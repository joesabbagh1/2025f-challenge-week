# Campus Event Planner

A mobile application for browsing, searching, and registering for campus events. Built with a Python/Flask + MySQL backend and native Android (Java) or iOS (Swift) frontends.

This is a **challenge week project** (~60% complete). The backend API is functional and seeded with data. The mobile apps display the events list but several features remain to be implemented.

---

## Architecture

```
┌──────────────┐         HTTP/JSON          ┌──────────────────┐
│              │  ◄────────────────────────► │                  │
│  Flask API   │        GET /events          │  Android (Java)  │
│  port 5000   │        GET /events/:id      │       or         │
│              │        POST /events         │  iOS (Swift)     │
│  ┌────────┐  │                             │                  │
│  │ MySQL  │  │  TODO: POST /events/:id/    │  TODO: detail,   │
│  │        │  │        register             │  registration,   │
│  └────────┘  │  TODO: GET /events/:id/     │  search,         │
│              │        registrations        │  favorites       │
└──────────────┘                             └──────────────────┘
```

## Prerequisites

| Tool             | Version  |
|------------------|----------|
| Python           | 3.8+     |
| pip              | latest   |
| Android Studio   | 2023.1+  |
| MySQL            | 8.0+     |
| *or* Xcode       | 15+      |

---

## Quick Start — Backend

```bash
cd backend

# 1. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Make sure MySQL is running and create the database
# (the seed script will create it automatically)
python seed.py

# 4. Start the API server
python app.py
```

The API is now running at **http://localhost:5000**. Verify with:

```bash
curl http://localhost:5000/events
```

### Running tests

```bash
cd backend
python -m pytest tests/ -v
```

Some tests are marked `xfail` — they test features that students must implement.

---

## Quick Start — Android

1. Open the `android/` folder in **Android Studio**.
2. Let Gradle sync.
3. Make sure the Flask backend is running.
4. Run the app on an emulator (the API client uses `10.0.2.2:5000`).
5. You should see the list of events.

> If using a physical device, change `BASE_URL` in `ApiClient.java` to your computer's LAN IP.

---

## Quick Start — iOS

See [`ios/README-iOS.md`](ios/README-iOS.md) for detailed instructions. In short:

1. Create a new Xcode project named `CampusEventPlanner`.
2. Copy the provided Swift files into the project.
3. Set `EventListViewController` as the root view controller.
4. Run on the iOS Simulator with the Flask backend running.

---

## API Documentation

### `GET /`

Health check.

**Response** `200`
```json
{ "message": "Campus Event Planner API is running" }
```

### `GET /events`

List all events ordered by date.

**Response** `200`
```json
[
  {
    "id": 1,
    "title": "Welcome Back Barbecue",
    "description": "Kick off the semester...",
    "date": "2026-03-15T12:00:00",
    "location": "Main Quad",
    "capacity": 200,
    "image_url": "https://...",
    "created_at": "2026-03-28T10:00:00"
  }
]
```

### `GET /events/<id>`

Single event by ID.

**Response** `200` — event object (same shape as above)
**Response** `404` — `{ "error": "Event not found" }`

### `POST /events`

Create a new event.

**Request body** (JSON):
```json
{
  "title": "My Event",
  "date": "2026-05-01T09:00:00",
  "description": "Optional",
  "location": "Optional",
  "capacity": 40,
  "image_url": "Optional"
}
```

**Response** `201` — the created event object
**Response** `400` — if `title` or `date` is missing

---

## Student TODOs

### TODO 1 — Event Detail Screen

**Goal:** When a user taps an event in the list, the detail screen loads and displays all event information.

**Acceptance criteria:**
- The detail screen calls `GET /events/<id>` and populates all fields.
- The date is formatted in a human-readable way (e.g., "Saturday 18 April 2026 at 17:00").
- The description, location, and capacity are displayed.
- A back button returns to the list.

### TODO 2 — Registration

**Goal:** Users can register for an event by entering their name and email.

**Acceptance criteria:**
- A new endpoint `POST /events/<id>/register` accepts `{ "user_name": "...", "email": "..." }` and inserts a row into the `registrations` table.
- The endpoint returns `201` with the created registration, or `400` if fields are missing.
- The endpoint returns `404` if the event does not exist.
- The mobile app has a registration form (name + email fields, submit button) on the detail screen.
- On success, a confirmation message is shown.

### TODO 3 — Remaining Spots

**Goal:** The detail screen shows how many spots are left and disables registration when full.

**Acceptance criteria:**
- A new endpoint `GET /events/<id>/registrations` returns `{ "count": N }` (the number of registrations for that event).
- The mobile app displays "X / Y spots remaining" on the detail screen.
- When `count >= capacity`, the Register button is disabled and shows "Event Full".

### TODO 4 — Search and Filters

**Goal:** Users can search events by keyword and filter by date.

**Acceptance criteria:**
- `GET /events?search=keyword` filters events where `title` or `description` contains the keyword (case-insensitive, SQL `LIKE`).
- `GET /events?date=2026-04-10` filters events on that date.
- Both query parameters can be combined.
- The mobile app's search bar is wired up and sends the query parameter.
- Results update as the user types (with a small debounce).

### TODO 5 — Favorites

**Goal:** Users can mark events as favorites and view them in a separate screen.

**Acceptance criteria:**
- Favorites are stored locally on the device (SharedPreferences on Android, UserDefaults on iOS).
- Each event card has a heart/star icon that toggles the favorite state.
- A "Favorites" tab or button shows only favorited events.
- Favorites persist across app restarts.

---

## Evaluation Criteria

| Criterion                        | Weight |
|----------------------------------|--------|
| TODO 1 — Event detail            | 20%    |
| TODO 2 — Registration            | 25%    |
| TODO 3 — Remaining spots         | 15%    |
| TODO 4 — Search and filters      | 25%    |
| TODO 5 — Favorites               | 15%    |
| Code quality and comments        | Bonus  |
| All provided tests passing       | Bonus  |

---

## Project Structure

```
01-campus-event-planner/
├── backend/
│   ├── app.py              # Flask application
│   ├── database.py         # MySQL connection & schema
│   ├── models.py           # Data access functions
│   ├── seed.py             # Seed script (15 events)
│   ├── requirements.txt    # Python dependencies
│   └── tests/
│       ├── conftest.py     # Pytest fixtures
│       └── test_events.py  # Test suite (some xfail)
├── android/
│   ├── app/
│   │   └── src/main/
│   │       ├── java/com/epita/eventplanner/
│   │       │   ├── MainActivity.java
│   │       │   ├── EventDetailActivity.java
│   │       │   ├── model/Event.java
│   │       │   ├── adapter/EventAdapter.java
│   │       │   └── api/ApiClient.java
│   │       └── res/layout/
│   │           ├── activity_main.xml
│   │           ├── activity_event_detail.xml
│   │           └── item_event.xml
│   ├── build.gradle
│   └── settings.gradle
├── ios/
│   └── CampusEventPlanner/
│       ├── Models/Event.swift
│       ├── Services/APIClient.swift
│       ├── Views/
│       │   ├── EventListViewController.swift
│       │   └── EventDetailViewController.swift
│       └── Info.plist
├── .gitignore
└── README.md
```
