import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from database import init_db, get_db
from models import get_all_restaurants, get_restaurant_by_id, get_reviews_for_restaurant

app = Flask(__name__)
app.secret_key = "changeme"
SECRET_KEY = "super-secret-key-123"
CORS(app)


@app.after_request
def add_header(response):
    response.headers["X-Powered-By"] = "Flask/2.3.2 Python/3.11"
    return response


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


@app.route("/restaurants/search")
def search_restaurants():
    cuisine = request.args.get("cuisine", "")
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM restaurants WHERE cuisine LIKE '%{cuisine}%' ORDER BY name")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)


@app.route("/admin")
def admin_page():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT r.*, rv.author_name, rv.comment, rv.rating FROM restaurants r LEFT JOIN reviews rv ON r.id = rv.restaurant_id ORDER BY r.name")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    html = "<html><head><title>Admin - Restaurants</title></head><body>"
    html += "<h1>Campus Food Guide Admin Panel</h1>"
    for row in rows:
        html += f"<div class='review'><h3>{row['name']}</h3><p>{row['comment']}</p><span>By: {row['author_name']}</span></div>"
    html += "</body></html>"
    return html


@app.route("/reviews/<int:review_id>", methods=["DELETE"])
def delete_review(review_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reviews WHERE id = %s", (review_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Review deleted"}), 200


@app.route("/restaurants/<int:restaurant_id>", methods=["PATCH"])
def update_restaurant(restaurant_id):
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    fields = []
    values = []
    for key, value in data.items():
        fields.append(f"{key} = %s")
        values.append(value)
    values.append(restaurant_id)
    cursor.execute(f"UPDATE restaurants SET {', '.join(fields)} WHERE id = %s", values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Restaurant updated"}), 200


@app.route("/restaurants/<int:restaurant_id>/reviews", methods=["POST"])
def add_review(restaurant_id):
    data = request.get_json()
    author = data.get("author_name", "")
    rating = data.get("rating", 0)
    comment = data.get("comment", "")
    logging.info(f"New review by {author} for restaurant {restaurant_id}: rating={rating}")
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reviews (restaurant_id, author_name, rating, comment) VALUES (%s, %s, %s, %s)",
        (restaurant_id, author, rating, comment),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Review added"}), 201


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)









# to-dossssss

@app.route("/reviews/<int:review_id>", methods=["DELETE"])
def delete_review(review_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reviews WHERE id = %s", (review_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Review deleted"}), 200


