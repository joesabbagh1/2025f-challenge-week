from flask import Flask, jsonify, request
from flask_cors import CORS

from database import init_db
from models import get_all_exercises, get_all_workouts, create_workout

app = Flask(__name__)
CORS(app)

# ---------------------------------------------------------------------------
# Initialise the database on startup
# ---------------------------------------------------------------------------
init_db()


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/exercises", methods=["GET"])
def list_exercises():
    """Return all exercises."""
    exercises = get_all_exercises()
    return jsonify(exercises)


@app.route("/workouts", methods=["GET"])
def list_workouts():
    """Return all workouts (date + duration, no exercises attached)."""
    workouts = get_all_workouts()
    return jsonify(workouts)


@app.route("/workouts", methods=["POST"])
def add_workout():
    """Create a basic workout.

    Expected JSON body:
        { "date": "2026-03-28", "duration_min": 45, "notes": "Leg day" }
    """
    data = request.get_json(force=True)
    if not data or "date" not in data:
        return jsonify({"error": "Missing required field: date"}), 400

    workout = create_workout(
        date=data["date"],
        duration_min=data.get("duration_min"),
        notes=data.get("notes"),
    )
    return jsonify(workout), 201


# ---------------------------------------------------------------------------
# TODO (students will implement these endpoints):
#   GET  /workouts/<id>          — workout detail with exercises (JOIN)
#   POST /workouts (extended)    — create workout WITH exercises in one request
#   GET  /stats                  — aggregate statistics (GROUP BY, COUNT, AVG)
#   GET  /workouts?from=&to=     — filter workouts by date range
#   DELETE /workouts/<id>        — delete a workout (CASCADE)
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True, port=5000)
