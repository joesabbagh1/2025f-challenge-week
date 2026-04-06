# Student Marketplace

A campus marketplace where students can buy and sell second-hand items. Built with a **Python/FastAPI** backend and a native mobile client (**Android/Java** or **iOS/Swift**).

This project is approximately **60% complete**. Your challenge: finish the remaining features during the build week.

---

## Architecture

```
┌──────────────┐         HTTP/JSON         ┌──────────────────┐
│              │  GET  /items              │                  │
│   Android    │  GET  /items/{id}        │   FastAPI        │
│     or       │◄─────────────────────────►│   Backend        │
│    iOS       │  POST /items             │   (Python)       │
│   Client     │  PATCH /items/{id} [TODO]│                  │
│              │                           │   MySQL DB       │
└──────────────┘                           └──────────────────┘
```

### What works now

- **Backend:** `GET /items`, `GET /items/{id}`, `POST /items` are fully functional.
- **Database:** MySQL with a seed script (20 realistic items across 4 categories).
- **Android:** Main screen displays the item list from the API. Navigation wired to detail and create screens.
- **iOS:** Table view displays items. Navigation wired to detail and create screens.

### What you need to build

See the [TODOs](#todos) section below.

---

## Prerequisites

| Tool | Version |
|------|---------|
| Python | 3.10+ |
| pip | latest |
| MySQL | 8.0+ |
| Android Studio | 2023.1+ (for Android track) |
| Xcode | 15+ (for iOS track) |

---

## Setup

### Backend

```bash
cd backend

# Make sure MySQL is running and accessible (default: root@localhost:3306)

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Seed the database with sample data (creates the DB and table automatically)
python seed.py

# Start the server
uvicorn app:app --reload --port 5000
```

The API is now available at `http://localhost:5000`.

### Android

1. Open the `android/` folder in **Android Studio**.
2. Let Gradle sync.
3. Make sure the backend is running on port 5000.
4. Run on an emulator (the app uses `10.0.2.2:5000` to reach host localhost).

### iOS

See [`ios/README-iOS.md`](ios/README-iOS.md) for detailed Xcode setup instructions.

---

## API Documentation

### `GET /items`

Returns all items, newest first.

```json
[
  {
    "id": 1,
    "title": "Introduction to Algorithms (Cormen, 4th ed.)",
    "description": "Hardcover, some highlighting in chapters 1-12.",
    "price": 35.0,
    "category": "Books",
    "image_url": null,
    "seller_name": "Alice Martin",
    "created_at": "2026-03-28 10:00:00",
    "is_sold": false
  }
]
```

### `GET /items/{id}`

Returns a single item. **404** if not found.

### `POST /items`

Create a new listing.

**Request body:**
```json
{
  "title": "My Item",
  "description": "Optional description",
  "price": 25.00,
  "category": "Books",
  "seller_name": "Your Name"
}
```

**Response:** `201 Created` with the full item object.

---

## Running Tests

```bash
cd backend
pytest tests/ -v
```

You should see **4 passing** and **3 failing** tests. The failing tests correspond to features you need to implement.

---

## TODOs

Each TODO includes **acceptance criteria** so you know when it is done.

### TODO 1 — Item Detail Screen

> **Goal:** Tapping an item in the list opens a detail view with all item info.

**Acceptance criteria:**
- Detail screen loads data from `GET /items/{id}`.
- Displays: title, description, price, category, seller name, posted date.
- If the item is sold, a visible "SOLD" badge is shown.
- Back navigation returns to the list.

**Files to edit:**
- Android: `ItemDetailActivity.java`, `activity_item_detail.xml`
- iOS: `ItemDetailViewController.swift`

---

### TODO 2 — Create Item Form + Validation

> **Goal:** The "+" button opens a form that lets the user post a new item.

**Acceptance criteria:**
- Form fields: title, description, price, category, seller name.
- Validation: title, price, category, and seller name are required. Price must be > 0.
- On submit, `POST /items` is called. On success, navigate back to the list. On error, display an error message.
- The new item appears in the list after returning.

**Files to edit:**
- Android: `CreateItemActivity.java`
- iOS: `CreateItemViewController.swift`

---

### TODO 3 — Filter by Category

> **Goal:** Users can filter the item list to show only one category.

**Acceptance criteria:**
- `GET /items?category=Books` returns only items where `category == "Books"`.
- The mobile app provides a UI control (dropdown, tab bar, or chips) to select a category.
- Selecting "All" (or equivalent) shows all items.
- Test `test_filter_by_category` passes.

**Files to edit:**
- Backend: `app.py`, `models.py`
- Android: `MainActivity.java`
- iOS: `ItemListViewController.swift`

---

### TODO 4 — Sort by Price / Date

> **Goal:** Users can sort items by price or date.

**Acceptance criteria:**
- `GET /items?sort=price_asc` returns items sorted by price ascending.
- Supported values: `price_asc`, `price_desc`, `date_asc`, `date_desc`.
- The mobile app provides a sort toggle or dropdown.
- Test `test_sort_items` passes.

**Files to edit:**
- Backend: `app.py`, `models.py`
- Android: `MainActivity.java`
- iOS: `ItemListViewController.swift`

---

### TODO 5 — Mark as Sold

> **Goal:** A seller can mark their item as sold.

**Acceptance criteria:**
- `PATCH /items/{id}` accepts `{"is_sold": true}` and updates the item.
- The detail screen shows a "Mark as sold" button (hidden if already sold).
- After marking as sold, the item appears dimmed in the list with a "SOLD" badge.
- Test `test_mark_as_sold` passes.

**Files to edit:**
- Backend: `app.py`, `models.py`
- Android: `ItemDetailActivity.java`, `activity_item_detail.xml`
- iOS: `ItemDetailViewController.swift`

---

### TODO 6 (Bonus) — Full-Text Search

> **Goal:** Users can search items by keyword.

**Acceptance criteria:**
- `GET /items?q=keyboard` returns items whose title or description contain "keyboard" (case-insensitive).
- The mobile app has a search bar at the top of the item list.
- Results update as the user types (or on submit).

**Files to edit:**
- Backend: `app.py`, `models.py`
- Android: `MainActivity.java`
- iOS: `ItemListViewController.swift`

---

## Project Structure

```
02-student-marketplace/
├── backend/
│   ├── app.py              # FastAPI application
│   ├── database.py         # MySQL connection helpers
│   ├── models.py           # Pydantic schemas + DB queries
│   ├── seed.py             # Seed 20 sample items
│   ├── requirements.txt    # Python dependencies
│   └── tests/
│       ├── conftest.py     # Test fixtures (test MySQL DB, TestClient)
│       └── test_items.py   # 7 tests (4 pass, 3 fail = your TODOs)
├── android/
│   ├── app/
│   │   └── src/main/
│   │       ├── java/com/epita/marketplace/
│   │       │   ├── MainActivity.java
│   │       │   ├── ItemDetailActivity.java      # TODO
│   │       │   ├── CreateItemActivity.java      # TODO
│   │       │   ├── model/Item.java
│   │       │   ├── adapter/ItemAdapter.java
│   │       │   └── api/ApiClient.java
│   │       ├── res/layout/
│   │       │   ├── activity_main.xml
│   │       │   ├── activity_item_detail.xml
│   │       │   ├── activity_create_item.xml
│   │       │   └── item_card.xml
│   │       └── AndroidManifest.xml
│   ├── app/build.gradle
│   ├── build.gradle
│   └── settings.gradle
├── ios/
│   ├── StudentMarketplace/
│   │   ├── Models/Item.swift
│   │   ├── Services/APIClient.swift
│   │   └── Views/
│   │       ├── ItemListViewController.swift
│   │       ├── ItemDetailViewController.swift   # TODO
│   │       └── CreateItemViewController.swift   # TODO
│   ├── StudentMarketplace/Info.plist
│   └── README-iOS.md
├── .gitignore
└── README.md
```
