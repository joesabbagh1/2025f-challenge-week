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


---

## SE TODOs (40)


### Core (01-15)

| Code | TODO |
|------|------|
| SFCD-S001 | [API] GET /decks/:id with card_count + difficulty counts |
| SFCD-S002 | [Mobile] Deck detail: name, desc, total, date |
| SFCD-S003 | [Mobile] Card list: question, difficulty color dot |
| SFCD-S004 | [Mobile] Empty deck: 'No cards yet' + button |
| SFCD-S005 | [API] PATCH /cards/:id {difficulty, last_reviewed} |
| SFCD-S006 | [Mobile] Fullscreen review: question centered |
| SFCD-S007 | [Mobile] Show Answer / tap-to-flip animation |
| SFCD-S008 | [Mobile] Easy/Medium/Hard buttons after reveal |
| SFCD-S009 | [Mobile] PATCH + auto-advance to next card |
| SFCD-S010 | [Mobile] Progress: 'Card 3 of 10' |
| SFCD-S011 | [Mobile] End summary: X easy, Y medium, Z hard |
| SFCD-S012 | [Mobile] Edge cases: 1-card, back during review |
| SFCD-S013 | [API] POST /decks/:id/cards {question, answer} |
| SFCD-S014 | [API] Validate: question 1-500, answer 1-2000 |
| SFCD-S015 | [Mobile] Add Card FAB: question + answer form |

### Intermediate (16-25)

| Code | TODO |
|------|------|
| SFCD-S016 | [Mobile] Client validation + char count |
| SFCD-S017 | [Mobile] On success, add to list, 'Add Another' |
| SFCD-S018 | [API] POST /decks/:id/cards/bulk (array, transaction) |
| SFCD-S019 | [Mobile] Bulk Import: paste Q|A pairs |
| SFCD-S020 | [API] GET /decks/:id/review?limit=10 (smart order) |
| SFCD-S021 | [API] mode param: hard/new/all |
| SFCD-S022 | [API] Return {cards, total_due, total_in_deck} |
| SFCD-S023 | [Mobile] Review button: 'Review (7 due)' |
| SFCD-S024 | [Mobile] Mode selector before review |
| SFCD-S025 | [Mobile] 'X more due — continue?' / 'Come back!' |

### Advanced (26-35)

| Code | TODO |
|------|------|
| SFCD-S026 | [API] GET /decks/:id/stats (reviewed, mastery, etc.) |
| SFCD-S027 | [Mobile] Stacked bar: green/orange/red proportions |
| SFCD-S028 | [Mobile] Mastery score as large percentage |
| SFCD-S029 | [Mobile] Tip if <5 cards |
| SFCD-S030 | [API] POST /decks {name, description} |
| SFCD-S031 | [Mobile] Create Deck: name + desc form |
| SFCD-S032 | [API] DELETE /decks/:id (cards first, transaction) |
| SFCD-S033 | [Mobile] Delete: long press, confirm, 'X cards' |
| SFCD-S034 | [API] PUT /cards/:id {question, answer} |
| SFCD-S035 | [Mobile] Edit card: pre-filled form |

### Polish (36-40)

| Code | TODO |
|------|------|
| SFCD-S036 | [Mobile] Search cards by question text |
| SFCD-S037 | [Mobile] Pull-to-refresh on deck + card lists |
| SFCD-S038 | [Mobile] Deck cards: name, count, mastery bar |
| SFCD-S039 | [Mobile] Streak counter: 'X days in a row!' |
| SFCD-S040 | [Mobile] Final polish: flip anim, colors, nav |

## CS TODOs (30)


### Threat Modeling (C001-C006)

| Code | TODO |
|------|------|
| SFCD-C001 | Architecture diagram + data flows + trust boundaries |
| SFCD-C002 | Endpoint inventory (method, inputs, auth, sensitivity) |
| SFCD-C003 | STRIDE analysis on main flow |
| SFCD-C004 | Attack surface mapping (all untrusted inputs) |
| SFCD-C005 | Attack tree (3+ paths, AND/OR nodes) |
| SFCD-C006 | 1-page threat assessment (top 5 risks) |

### Code Review / Bug Bounty (C007-C016)

| Code | TODO |
|------|------|
| SFCD-C007 | Find SQL Injection (CWE-89) |
| SFCD-C008 | Find Stored XSS (CWE-79) |
| SFCD-C009 | Find IDOR (CWE-639) |
| SFCD-C010 | Find hardcoded secrets (CWE-798) |
| SFCD-C011 | Find weak password hashing (CWE-328) |
| SFCD-C012 | Audit missing authentication (CWE-306) |
| SFCD-C013 | Analyze CORS configuration |
| SFCD-C014 | Find debug mode exposure (CWE-489) |
| SFCD-C015 | Review error handling (CWE-209) |
| SFCD-C016 | Audit SE teammates' code (2+ bug reports) |

### Security Testing (C017-C024)

| Code | TODO |
|------|------|
| SFCD-C017 | SQLi exploit script |
| SFCD-C018 | XSS exploit (3 payloads) |
| SFCD-C019 | IDOR enumeration script |
| SFCD-C020 | Rate limit / DoS test |
| SFCD-C021 | Automated scan (nmap + Python) |
| SFCD-C022 | API fuzzer |
| SFCD-C023 | Project-specific exploit (Werkzeug/pickle/CSRF/etc.) |
| SFCD-C024 | test_security.py (8+ pytest cases) |

### Deployment & Hardening (C025-C030)

| Code | TODO |
|------|------|
| SFCD-C025 | Fix SQL Injection (parameterized queries) |
| SFCD-C026 | Add authentication + fix IDOR |
| SFCD-C027 | Secure configuration (debug, secrets, passwords) |
| SFCD-C028 | Security headers + rate limiting |
| SFCD-C029 | Structured logging + alerting |
| SFCD-C030 | Final 5-page audit report |
