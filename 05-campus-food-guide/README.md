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
