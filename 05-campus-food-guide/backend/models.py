from database import get_db


def _serialize_row(row):
    """Convert datetime objects to strings for JSON serialization."""
    if row is None:
        return None
    d = dict(row)
    for key, value in d.items():
        if hasattr(value, 'isoformat'):
            d[key] = value.isoformat()
    return d


def get_all_restaurants():
    """Return all restaurants with their average rating computed via SQL."""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT r.id, r.name, r.cuisine, r.address, r.price_range, r.image_url,
               ROUND(AVG(rev.rating), 1) AS avg_rating,
               COUNT(rev.id) AS review_count
        FROM restaurants r
        LEFT JOIN reviews rev ON r.id = rev.restaurant_id
        GROUP BY r.id
        ORDER BY r.name
    """)
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return [_serialize_row(r) for r in rows]


def get_restaurant_by_id(restaurant_id):
    """Return a single restaurant by its ID with average rating."""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT r.id, r.name, r.cuisine, r.address, r.price_range, r.image_url,
               ROUND(AVG(rev.rating), 1) AS avg_rating,
               COUNT(rev.id) AS review_count
        FROM restaurants r
        LEFT JOIN reviews rev ON r.id = rev.restaurant_id
        WHERE r.id = %s
        GROUP BY r.id
    """, (restaurant_id,))
    row = cursor.fetchone()
    cursor.close()
    db.close()
    return _serialize_row(row)


def get_reviews_for_restaurant(restaurant_id):
    """Return all reviews for a given restaurant."""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, restaurant_id, author_name, rating, comment, created_at
        FROM reviews
        WHERE restaurant_id = %s
        ORDER BY created_at DESC
    """, (restaurant_id,))
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return [_serialize_row(r) for r in rows]
