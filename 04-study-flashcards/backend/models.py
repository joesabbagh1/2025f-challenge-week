"""Pydantic models and database query functions for Study Flashcards."""

from pydantic import BaseModel
from typing import Optional
from database import get_db


# ---------------------------------------------------------------------------
# Pydantic schemas
# ---------------------------------------------------------------------------

class DeckCreate(BaseModel):
    name: str
    description: Optional[str] = None


class DeckResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    created_at: str
    card_count: int = 0


class CardResponse(BaseModel):
    id: int
    deck_id: int
    question: str
    answer: str
    difficulty: int
    last_reviewed: Optional[str]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _serialize_row(row):
    """Convert datetime objects in a row dict to strings."""
    if row is None:
        return None
    d = dict(row)
    for key, value in d.items():
        if hasattr(value, 'isoformat'):
            d[key] = value.isoformat()
    return d


# ---------------------------------------------------------------------------
# Query helpers
# ---------------------------------------------------------------------------

def fetch_all_decks(db_name: str | None = None) -> list[dict]:
    """Return every deck with its card count."""
    db = get_db(db_name)
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT d.id, d.name, d.description, d.created_at,
               COUNT(c.id) AS card_count
        FROM decks d
        LEFT JOIN cards c ON c.deck_id = d.id
        GROUP BY d.id
        ORDER BY d.id
    """)
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return [_serialize_row(r) for r in rows]


def fetch_deck_by_id(deck_id: int, db_name: str | None = None) -> dict | None:
    """Return a single deck with its card count, or None."""
    db = get_db(db_name)
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT d.id, d.name, d.description, d.created_at,
               COUNT(c.id) AS card_count
        FROM decks d
        LEFT JOIN cards c ON c.deck_id = d.id
        WHERE d.id = %s
        GROUP BY d.id
    """, (deck_id,))
    row = cursor.fetchone()
    cursor.close()
    db.close()
    return _serialize_row(row)


def fetch_cards_for_deck(deck_id: int, db_name: str | None = None) -> list[dict]:
    """Return all cards belonging to a deck."""
    db = get_db(db_name)
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, deck_id, question, answer, difficulty, last_reviewed
        FROM cards
        WHERE deck_id = %s
        ORDER BY id
    """, (deck_id,))
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return [_serialize_row(r) for r in rows]


def create_deck(data: DeckCreate, db_name: str | None = None) -> dict:
    """Insert a new deck and return it."""
    db = get_db(db_name)
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "INSERT INTO decks (name, description) VALUES (%s, %s)",
        (data.name, data.description),
    )
    db.commit()
    deck_id = cursor.lastrowid
    cursor.execute("""
        SELECT d.id, d.name, d.description, d.created_at,
               COUNT(c.id) AS card_count
        FROM decks d
        LEFT JOIN cards c ON c.deck_id = d.id
        WHERE d.id = %s
        GROUP BY d.id
    """, (deck_id,))
    row = cursor.fetchone()
    cursor.close()
    db.close()
    return _serialize_row(row)
