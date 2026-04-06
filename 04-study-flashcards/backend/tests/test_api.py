"""API tests for Study Flashcards.

Tests marked SHOULD FAIL correspond to endpoints that students must implement.
"""


# -----------------------------------------------------------------------
# Provided (should pass)
# -----------------------------------------------------------------------

def test_get_decks(client):
    """GET /decks returns all 5 seeded decks."""
    resp = client.get("/decks")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 5
    names = {d["name"] for d in data}
    assert names == {"Python", "SQL", "Algorithms", "Unix", "Networks"}


def test_get_deck_by_id(client):
    """GET /decks/1 returns the deck with its card_count."""
    resp = client.get("/decks/1")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1
    assert data["card_count"] == 10


def test_get_deck_cards(client):
    """GET /decks/1/cards returns 10 cards."""
    resp = client.get("/decks/1/cards")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 10
    assert "question" in data[0]
    assert "answer" in data[0]


def test_create_deck(client):
    """POST /decks creates a new deck."""
    resp = client.post("/decks", json={"name": "Test Deck", "description": "A test"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "Test Deck"
    assert data["card_count"] == 0


# -----------------------------------------------------------------------
# TODO -- students must implement these endpoints (tests SHOULD FAIL)
# -----------------------------------------------------------------------

def test_review_cards(client):
    """PATCH /cards/:id -- update difficulty and last_reviewed after review."""
    resp = client.patch("/cards/1", json={"difficulty": 3})
    assert resp.status_code == 200
    data = resp.json()
    assert data["difficulty"] == 3
    assert data["last_reviewed"] is not None


def test_smart_review(client):
    """GET /decks/:id/review?limit=10 -- prioritize hard & least-recently-reviewed cards."""
    resp = client.get("/decks/1/review?limit=5")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) <= 5
    assert "question" in data[0]


def test_deck_stats(client):
    """GET /decks/:id/stats -- return card counts grouped by difficulty."""
    resp = client.get("/decks/1/stats")
    assert resp.status_code == 200
    data = resp.json()
    assert "total" in data
    assert "by_difficulty" in data


def test_add_card(client):
    """POST /decks/:id/cards -- add a new card to a deck."""
    resp = client.post(
        "/decks/1/cards",
        json={"question": "What is PEP8?", "answer": "Python style guide.", "difficulty": 1},
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["question"] == "What is PEP8?"
    assert data["deck_id"] == 1
