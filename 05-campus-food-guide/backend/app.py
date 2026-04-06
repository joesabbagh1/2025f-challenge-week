from flask import Flask, jsonify
from flask_cors import CORS
from database import init_db
from models import get_all_restaurants, get_restaurant_by_id, get_reviews_for_restaurant

app = Flask(__name__)
CORS(app)


@app.route("/restaurants", methods=["GET"])
def list_restaurants():
    """Return all restaurants with average ratings."""
    restaurants = get_all_restaurants()
    return jsonify(restaurants)


@app.route("/restaurants/<int:restaurant_id>", methods=["GET"])
def restaurant_detail(restaurant_id):
    """Return a single restaurant by ID."""
    restaurant = get_restaurant_by_id(restaurant_id)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(restaurant)


@app.route("/restaurants/<int:restaurant_id>/reviews", methods=["GET"])
def restaurant_reviews(restaurant_id):
    """Return all reviews for a restaurant."""
    restaurant = get_restaurant_by_id(restaurant_id)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404
    reviews = get_reviews_for_restaurant(restaurant_id)
    return jsonify(reviews)


# ---------------------------------------------------------------------------
# TODO: POST /restaurants/<id>/reviews  -- add a new review
# TODO: GET  /restaurants/<id>/stats    -- rating statistics (avg, count, distribution)
# TODO: GET  /restaurants?cuisine=      -- filter by cuisine
# TODO: GET  /restaurants?sort=         -- sort (rating, review_count, name)
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)
