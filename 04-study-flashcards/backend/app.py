"""Study Flashcards -- FastAPI backend.

Provides a REST API for managing flashcard decks and cards.
Students will extend this with additional endpoints during the build week.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import init_db
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

app = FastAPI(title="Study Flashcards API", version="0.1.0")

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


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
