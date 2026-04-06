# Fitness Tracker

A workout tracking application with a Python/Flask + MySQL backend and native mobile frontends (Android or iOS).

## Project structure

```
backend/          Python/Flask API + MySQL database
android/          Android app (Java)
ios/              iOS app (Swift)
```

## Prerequisites

- Python 3.10+
- MySQL 8.0+ (must be installed and running)

## Getting started

### Backend

Make sure MySQL is running locally before starting the backend. By default the app connects as `root` with no password to a database called `fitness_tracker`. You can override this with environment variables: `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`.

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python seed.py             # populate the database with sample data
python app.py              # starts on http://localhost:5000
```

### Android

1. Open the `android/` folder in Android Studio.
2. Make sure the backend is running.
3. Run the app on an emulator (the API client uses `10.0.2.2:5000` to reach the host).

### iOS

1. See `ios/README-iOS.md` for Xcode setup instructions.
2. Make sure the backend is running on `localhost:5000`.
3. Run the app on the iOS Simulator.

## API endpoints (implemented)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/exercises` | List all exercises |
| GET | `/workouts` | List all workouts (date + duration) |
| POST | `/workouts` | Create a basic workout (`{ "date", "duration_min", "notes" }`) |

## Running the tests

```bash
cd backend
pytest -v
```

Three tests pass out of the box. Five tests are expected to fail — they cover features you will build during the week.

---

## TODO — Build Week Tasks

### TODO 1: Workout detail

**Backend:** Add `GET /workouts/<id>` that returns the workout together with its exercises. Use a JOIN query across `workouts` and `workout_exercises` and `exercises` to build the response.

**Mobile:** When the user taps a workout in the history list, navigate to the detail screen (`WorkoutDetailActivity` / `WorkoutDetailViewController`) and display the list of exercises with sets, reps, and weight.

**Test:** `test_workout_detail`

---

### TODO 2: Create a full workout

**Backend:** Extend `POST /workouts` so that when the request body contains an `exercises` array, each entry is inserted into `workout_exercises` inside a single database transaction. Roll back if anything fails.

Example request body:
```json
{
  "date": "2026-03-28",
  "duration_min": 60,
  "notes": "Push day",
  "exercises": [
    { "exercise_id": 1, "sets": 4, "reps": 8, "weight_kg": 70.0 },
    { "exercise_id": 5, "sets": 3, "reps": 10, "weight_kg": 50.0 }
  ]
}
```

**Mobile:** Build a "New Workout" screen where the user picks exercises from the list, enters sets/reps/weight for each, and submits the whole workout.

**Test:** `test_create_workout_with_exercises`

---

### TODO 3: Statistics

**Backend:** Add `GET /stats` that returns aggregate data using SQL `GROUP BY`, `COUNT`, and `AVG`:
- `total_workouts` — total number of workouts
- `total_duration_min` — sum of all workout durations
- `avg_duration_min` — average workout duration
- `workouts_per_category` — number of workouts that include at least one exercise from each category

**Mobile:** Add a Statistics screen (new tab or button) that displays the stats in a readable layout (cards, simple charts, or formatted text).

**Test:** `test_stats`

---

### TODO 4: Filter workouts by date range

**Backend:** Update `GET /workouts` to accept optional `from` and `to` query parameters. When provided, filter workouts using `WHERE date >= %s AND date <= %s`.

**Mobile:** Add a date-range picker (two date pickers or preset buttons like "This week" / "This month" / "All") above the workout history list. Re-fetch the list with the selected range.

**Test:** `test_filter_workouts_by_date`

---

### TODO 5: Delete a workout

**Backend:** Add `DELETE /workouts/<id>`. Delete the workout and all its linked `workout_exercises` rows. Use `ON DELETE CASCADE` or explicit deletes inside a transaction.

**Mobile:** Add a delete action to the workout detail or history screen (swipe-to-delete, long press, or a button). Show a confirmation dialog before deleting.

**Test:** `test_delete_workout`
