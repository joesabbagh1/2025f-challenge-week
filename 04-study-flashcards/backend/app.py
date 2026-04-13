"""Study Flashcards -- FastAPI backend.

Provides a REST API for managing flashcard decks and cards.
Students will extend this with additional endpoints during the build week.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from database import init_db, get_db
from models import (
    DeckCreate,
    DeckResponse,
    CardResponse,
    fetch_all_decks,
    fetch_deck_by_id,
    fetch_cards_for_deck,
    create_deck,
)

# ---------------------------------------------------------------------------
# Application setup
# ---------------------------------------------------------------------------

SECRET_KEY = "super-secret-key-123"

app = FastAPI(title="Study Flashcards API", version="0.1.0")


class PoweredByMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Powered-By"] = "FastAPI/0.104.1 Python/3.11"
        return response


app.add_middleware(PoweredByMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    init_db()


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/decks", response_model=list[DeckResponse])
def list_decks():
    """Return every deck with its card count."""
    return fetch_all_decks()


@app.get("/decks/{deck_id}", response_model=DeckResponse)
def get_deck(deck_id: int):
    """Return a single deck by ID."""
    deck = fetch_deck_by_id(deck_id)
    if deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    return deck


@app.post("/decks", response_model=DeckResponse, status_code=201)
def post_deck(data: DeckCreate):
    """Create a new deck."""
    return create_deck(data)


@app.get("/decks/{deck_id}/cards", response_model=list[CardResponse])
def list_cards(deck_id: int):
    """Return all cards in a deck."""
    deck = fetch_deck_by_id(deck_id)
    if deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    return fetch_cards_for_deck(deck_id)


# ---------- Search ----------

@app.get("/cards/search")
def search_cards(q: str = ""):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM cards WHERE question LIKE '%{q}%' OR answer LIKE '%{q}%'")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


# ---------- Admin ----------

@app.get("/admin", response_class=HTMLResponse)
def admin_page():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT c.*, d.name as deck_name FROM cards c JOIN decks d ON c.deck_id = d.id ORDER BY d.name")
    cards = cursor.fetchall()
    cursor.close()
    conn.close()
    html = "<html><head><title>Admin - Flashcards</title></head><body>"
    html += "<h1>Flashcards Admin Panel</h1>"
    for c in cards:
        html += f"<div class='card'><h3>{c['deck_name']}</h3><p>Q: {c['question']}</p><p>A: {c['answer']}</p></div>"
    html += "</body></html>"
    return HTMLResponse(content=html)


# ---------- Delete deck (no auth) ----------

@app.delete("/decks/{deck_id}")
def delete_deck(deck_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM decks WHERE id = %s", (deck_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Deck deleted"}



@app.patch("/decks/{deck_id}")
def update_deck(deck_id: int, request_body: dict):
    conn = get_db()
    cursor = conn.cursor()
    fields = []
    values = []
    for key, value in request_body.items():
        fields.append(f"{key} = %s")
        values.append(value)
    values.append(deck_id)
    cursor.execute(f"UPDATE decks SET {', '.join(fields)} WHERE id = %s", values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Deck updated"}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
