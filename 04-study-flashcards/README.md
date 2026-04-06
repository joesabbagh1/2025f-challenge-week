# Study Flashcards

A spaced-repetition flashcard app for CS students. Review decks of questions, flip cards to reveal answers, and rate difficulty to prioritize what you study next.

**Stack:** Python / FastAPI + MySQL (backend) | Android (Java) or iOS (Swift) (mobile)

## Quick start

### Prerequisites

- **MySQL 8+** running on `localhost:3306` (default). Configure via environment variables: `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`.

### Backend

```bash
cd backend
pip install -r requirements.txt
python seed.py          # creates the study_flashcards database with 5 decks, 50 cards
python app.py           # starts the API on http://localhost:5000
```

Verify it works:

```bash
curl http://localhost:5000/decks
```

### Android

1. Open the `android/` folder in Android Studio.
2. Make sure the backend is running on your machine.
3. Run on an emulator (the API client uses `10.0.2.2:5000` which maps to host localhost).

### iOS

See `ios/README-iOS.md`.

## Running tests

```bash
cd backend
pip install -r requirements.txt
pytest tests/ -v
```

The first 4 tests should **pass**. The last 4 should **fail** -- those are the endpoints you need to implement.

---

## What is already built

| Layer | What works |
|-------|-----------|
| **Backend** | `GET /decks`, `GET /decks/{id}`, `POST /decks`, `GET /decks/{id}/cards` |
| **Android** | Main screen lists decks from the API via RecyclerView. `FlipAnimationHelper` is provided and ready to use. |
| **iOS** | Deck list screen fetches and displays decks. `FlipAnimationHelper` UIView extension is provided. |

---

## TODOs

### TODO 1 -- Deck screen (show cards)

**Goal:** When the user taps a deck, display its cards.

- **Mobile:** In `DeckActivity` (Android) or `DeckDetailViewController` (iOS), call `GET /decks/{id}/cards` and display results in a list.
- **Hint:** Create a `CardAdapter` (Android) or use a `UITableView` data source (iOS).

### TODO 2 -- Review mode

**Goal:** Let the user review cards one at a time with a flip animation.

- **Mobile:** In `ReviewActivity` / `ReviewViewController`, load cards for the deck. Show the question, tap to flip and reveal the answer. The `FlipAnimationHelper` is already provided -- see its documentation for usage.
- **Backend:** Implement `PATCH /cards/{id}` to update `difficulty` (1/2/3) and set `last_reviewed` to the current timestamp.
- **Mobile:** After flipping, show three buttons (Easy / Medium / Hard). Send a PATCH request, then move to the next card.

### TODO 3 -- Add cards

**Goal:** Let the user add new cards to a deck.

- **Backend:** Implement `POST /decks/{id}/cards` accepting `{ "question": "...", "answer": "...", "difficulty": 1 }`.
- **Mobile:** Add an "Add Card" button on the deck screen with a form (two text fields + optional difficulty picker). POST to the API and refresh the list.

### TODO 4 -- Smart review

**Goal:** Prioritize cards the user struggles with and hasn't reviewed recently.

- **Backend:** Implement `GET /decks/{id}/review?limit=10`. Return cards ordered by `difficulty DESC, last_reviewed ASC NULLS FIRST`. Limit defaults to 10.
- **Mobile:** Add a "Smart Review" button that uses this endpoint instead of fetching all cards.

### TODO 5 -- Deck stats

**Goal:** Show study progress for a deck.

- **Backend:** Implement `GET /decks/{id}/stats` returning:
  ```json
  {
    "total": 10,
    "reviewed": 7,
    "by_difficulty": { "1": 4, "2": 3, "3": 3 }
  }
  ```
  Use `GROUP BY difficulty` and count cards where `last_reviewed IS NOT NULL`.
- **Mobile:** Display the stats on the deck screen (counters, progress bar, or a simple chart).

### TODO 6 (Bonus) -- Create deck from mobile

**Goal:** Let the user create a new deck from the app.

- The `POST /decks` endpoint already exists.
- **Mobile:** Add a "New Deck" button or FAB. Show a dialog/form with name and description fields. POST to the API and refresh the deck list.

---

## API reference

### Implemented

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/decks` | List all decks (with card count) |
| GET | `/decks/{id}` | Get a single deck |
| POST | `/decks` | Create a deck (`{ "name": "...", "description": "..." }`) |
| GET | `/decks/{id}/cards` | List all cards in a deck |

### To implement

| Method | Endpoint | Description |
|--------|----------|-------------|
| PATCH | `/cards/{id}` | Update a card's difficulty and last_reviewed |
| POST | `/decks/{id}/cards` | Add a card to a deck |
| GET | `/decks/{id}/review?limit=10` | Smart review (hard + stale cards first) |
| GET | `/decks/{id}/stats` | Deck statistics grouped by difficulty |

## Database schema

```sql
CREATE TABLE decks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    deck_id INT NOT NULL,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    difficulty INT DEFAULT 1,  -- 1=easy, 2=medium, 3=hard
    last_reviewed VARCHAR(30),
    FOREIGN KEY (deck_id) REFERENCES decks(id) ON DELETE CASCADE
);
```
