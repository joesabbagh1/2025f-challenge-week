# Campus Food Guide

A mobile app to discover and review restaurants near campus. Built with a **Python/Flask** backend and an **Android (Java)** or **iOS (Swift)** frontend.

## Architecture

```
backend/          Python/Flask REST API + MySQL database
android/          Android app (Java, RecyclerView, Material Design)
ios/              iOS app (Swift, UIKit, SF Symbols)
```

## Getting started

### Prerequisites

- **MySQL 8.0+** must be installed and running on `localhost:3306`
- The backend connects as `root` with no password by default. Override with environment variables: `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`.

### 1. Backend

```bash
cd backend
pip install -r requirements.txt
python seed.py          # Creates the database and seeds 12 restaurants + 40 reviews
python app.py           # Starts the API on http://localhost:5000
```

### 2. Mobile app

**Android:** Open the `android/` folder in Android Studio. The app connects to `10.0.2.2:5000` (emulator loopback to host). Run on an emulator.

**iOS:** Open the Xcode project in `ios/`. The app connects to `localhost:5000`. Run on the Simulator.

## API reference (what exists)

| Method | Endpoint                        | Description                          |
|--------|---------------------------------|--------------------------------------|
| GET    | `/restaurants`                  | List all restaurants with avg_rating |
| GET    | `/restaurants/<id>`             | Single restaurant detail             |
| GET    | `/restaurants/<id>/reviews`     | List reviews for a restaurant        |

## Running the tests

```bash
cd backend
pytest tests/ -v
```

Four tests pass (list, detail, reviews, 404). Four tests **intentionally fail** -- they cover features you need to build.

---

## Your TODOs (5 features to implement)

### TODO 1 -- Full detail screen (load and display reviews)

The detail screen (`RestaurantDetailActivity` / `RestaurantDetailViewController`) shows restaurant info but **does not load reviews yet**.

**What to do:**
- Call `GET /restaurants/<id>/reviews` from the detail screen
- Parse the JSON response into a list of `Review` objects
- Use the provided `ReviewAdapter` (Android) or create review subviews (iOS) to display each review with: author name, star rating, comment, and date
- Hide the placeholder text once reviews are loaded

**Hints:**
- Android: `ReviewAdapter` is already written. Create an instance, set it on `reviewsRecycler`, and call `setReviews()`.
- iOS: `StarRatingView` is provided. Use it for each review's rating display.

---

### TODO 2 -- Rating statistics endpoint and display

Create a new endpoint that returns detailed rating statistics for a restaurant.

**Backend -- `GET /restaurants/<id>/stats`:**
```json
{
  "average": 4.2,
  "total": 15,
  "distribution": {
    "1": 0,
    "2": 1,
    "3": 2,
    "4": 7,
    "5": 5
  }
}
```

Use SQL `COUNT` with `GROUP BY rating` to compute the distribution.

**Mobile -- display the stats:**
- Show the average rating prominently
- Display a horizontal bar chart for the distribution (5 bars, one per star level)
- Show total review count

---

### TODO 3 -- Add a review (form + POST endpoint)

Allow users to submit a review for a restaurant.

**Backend -- `POST /restaurants/<id>/reviews`:**
- Accept JSON body: `{ "author_name": "...", "rating": 4, "comment": "..." }`
- Validate: `author_name` required, `rating` between 1-5
- Insert into the database and return the created review with status `201`

**Mobile -- review form:**
- Add a button (e.g. floating action button or "Write a review" button)
- Show a form with: name field, star selector (tap to rate 1-5), comment field
- Submit via POST, then refresh the reviews list

---

### TODO 4 -- Filter restaurants by cuisine and price

Add query parameter support to the restaurant list endpoint.

**Backend -- update `GET /restaurants`:**
- `?cuisine=Japanese` -- filter by cuisine (case-insensitive)
- `?price=1` -- filter by price range
- Both can be combined: `?cuisine=Thai&price=1`

**Mobile -- filter UI:**
- Add a cuisine dropdown, chip group, or segmented control
- Add a price range selector (1-3 euros)
- Re-fetch the restaurant list with the selected filters

---

### TODO 5 -- Sort restaurants

Add sorting support to the restaurant list.

**Backend -- update `GET /restaurants`:**
- `?sort=rating` -- sort by average rating (descending)
- `?sort=reviews` -- sort by review count (descending)
- `?sort=name` -- sort alphabetically (ascending)

**Mobile -- sort UI:**
- Add a sort toggle or dropdown in the toolbar / header
- Re-fetch with the selected sort parameter

---

## Database schema

```sql
CREATE TABLE restaurants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cuisine VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    price_range INT DEFAULT 2,
    image_url TEXT
);

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    author_name VARCHAR(255) NOT NULL,
    rating INT NOT NULL,
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
);
```

## Sample restaurants

| Name              | Cuisine    | Price |
|-------------------|------------|-------|
| Sakura Ramen      | Japanese   | $$    |
| Bella Napoli      | Italian    | $$    |
| Le Petit Bistrot  | French     | $$$   |
| Bangkok Express   | Thai       | $     |
| Casa Mexicana     | Mexican    | $     |
| Taj Palace        | Indian     | $$    |
| Dragon d'Or       | Chinese    | $     |
| The Campus Diner  | American   | $$    |
| Seoul Kitchen     | Korean     | $$    |
| Beirut Mezze      | Lebanese   | $$    |
| Pho Saigon        | Vietnamese | $     |
| Olympus Taverna   | Greek      | $$    |


---

## SE TODOs (40)


### Core (01-15)

| Code | TODO |
|------|------|
| CFGD-S001 | [API] GET /restaurants/:id/reviews (ordered by date) |
| CFGD-S002 | [API] GET /restaurants/:id with review_count + avg_rating |
| CFGD-S003 | [Mobile] Detail: name, cuisine, address, price, stars, count |
| CFGD-S004 | [Mobile] Reviews list: author, stars, comment, date |
| CFGD-S005 | [Mobile] Long comments: truncate + 'Read more' |
| CFGD-S006 | [Mobile] Empty: 'No reviews yet — be the first!' |
| CFGD-S007 | [API] GET /restaurants/:id/stats (avg, count, distribution) |
| CFGD-S008 | [API] Fill missing ratings with 0 in distribution |
| CFGD-S009 | [Mobile] Rating summary: avg + stars + 'Based on X' |
| CFGD-S010 | [Mobile] 5 horizontal bars: green→red + count |
| CFGD-S011 | [API] POST /restaurants/:id/reviews with validation |
| CFGD-S012 | [API] Return 400/201 with field errors / updated avg |
| CFGD-S013 | [Mobile] 'Write a Review' button |
| CFGD-S014 | [Mobile] Form: name, star widget, comment + counter |
| CFGD-S015 | [Mobile] Inline validation + remember author name |

### Intermediate (16-25)

| Code | TODO |
|------|------|
| CFGD-S016 | [Mobile] On success: add review, update avg + bars |
| CFGD-S017 | [API] GET /cuisines (DISTINCT) |
| CFGD-S018 | [API] GET /restaurants with cuisine + price params |
| CFGD-S019 | [Mobile] Cuisine chips from GET /cuisines |
| CFGD-S020 | [Mobile] Price toggles: $, $$, $$$ |
| CFGD-S021 | [Mobile] Filter count + 'Clear all' + empty state |
| CFGD-S022 | [API] sort param: rating, reviews, name, price |
| CFGD-S023 | [API] Sort with LEFT JOIN + AVG for ratings |
| CFGD-S024 | [API] Combine sort + cuisine + price filters |
| CFGD-S025 | [Mobile] Sort dropdown: Best Rated, Most Reviewed, etc. |

### Advanced (26-35)

| Code | TODO |
|------|------|
| CFGD-S026 | [Mobile] Active sort label + persist preference |
| CFGD-S027 | [Mobile] List cards: image, name, cuisine, price, stars |
| CFGD-S028 | [API] Pagination: page + limit + total_count |
| CFGD-S029 | [Mobile] Infinite scroll + loading indicator |
| CFGD-S030 | [Mobile] Pull-to-refresh |
| CFGD-S031 | [Mobile] Share button on detail |
| CFGD-S032 | [Mobile] Bookmark feature + Bookmarks screen |
| CFGD-S033 | [API] GET /restaurants/top?limit=5 |
| CFGD-S034 | [Mobile] 'Top Rated' carousel at top |
| CFGD-S035 | [Mobile] Image loading + placeholders |

### Polish (36-40)

| Code | TODO |
|------|------|
| CFGD-S036 | [Mobile] Map section + 'Open in Maps' button |
| CFGD-S037 | [Mobile] 'Report Review' flag button |
| CFGD-S038 | [API] GET /reviews?sort=helpful/newest |
| CFGD-S039 | [Mobile] Review sort toggle: Newest/Highest |
| CFGD-S040 | [Mobile] Final polish: stars, price icons, spacing |

## CS TODOs (30)


### Threat Modeling (C001-C006)

| Code | TODO |
|------|------|
| CFGD-C001 | Architecture diagram + data flows + trust boundaries |
| CFGD-C002 | Endpoint inventory (method, inputs, auth, sensitivity) |
| CFGD-C003 | STRIDE analysis on main flow |
| CFGD-C004 | Attack surface mapping (all untrusted inputs) |
| CFGD-C005 | Attack tree (3+ paths, AND/OR nodes) |
| CFGD-C006 | 1-page threat assessment (top 5 risks) |

### Code Review / Bug Bounty (C007-C016)

| Code | TODO |
|------|------|
| CFGD-C007 | Find SQL Injection (CWE-89) |
| CFGD-C008 | Find Stored XSS (CWE-79) |
| CFGD-C009 | Find IDOR (CWE-639) |
| CFGD-C010 | Find hardcoded secrets (CWE-798) |
| CFGD-C011 | Find weak password hashing (CWE-328) |
| CFGD-C012 | Audit missing authentication (CWE-306) |
| CFGD-C013 | Analyze CORS configuration |
| CFGD-C014 | Find debug mode exposure (CWE-489) |
| CFGD-C015 | Review error handling (CWE-209) |
| CFGD-C016 | Audit SE teammates' code (2+ bug reports) |

### Security Testing (C017-C024)

| Code | TODO |
|------|------|
| CFGD-C017 | SQLi exploit script |
| CFGD-C018 | XSS exploit (3 payloads) |
| CFGD-C019 | IDOR enumeration script |
| CFGD-C020 | Rate limit / DoS test |
| CFGD-C021 | Automated scan (nmap + Python) |
| CFGD-C022 | API fuzzer |
| CFGD-C023 | Project-specific exploit (Werkzeug/pickle/CSRF/etc.) |
| CFGD-C024 | test_security.py (8+ pytest cases) |

### Deployment & Hardening (C025-C030)

| Code | TODO |
|------|------|
| CFGD-C025 | Fix SQL Injection (parameterized queries) |
| CFGD-C026 | Add authentication + fix IDOR |
| CFGD-C027 | Secure configuration (debug, secrets, passwords) |
| CFGD-C028 | Security headers + rate limiting |
| CFGD-C029 | Structured logging + alerting |
| CFGD-C030 | Final 5-page audit report |
