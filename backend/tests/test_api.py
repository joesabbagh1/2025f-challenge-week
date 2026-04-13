"""API tests for the Campus Food Guide backend.

Tests marked with 'should_fail' exercise endpoints that students must implement.
"""

import json


def test_get_restaurants(client):
    """GET /restaurants returns a list of restaurants with avg_rating."""
    response = client.get("/restaurants")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 12

    # Each restaurant should have computed fields
    first = data[0]
    assert "id" in first
    assert "name" in first
    assert "cuisine" in first
    assert "avg_rating" in first
    assert "review_count" in first


def test_get_restaurant_by_id(client):
    """GET /restaurants/<id> returns a single restaurant."""
    response = client.get("/restaurants/1")
    assert response.status_code == 200

    data = response.get_json()
    assert data["id"] == 1
    assert data["name"] == "Sakura Ramen"
    assert data["cuisine"] == "Japanese"
    assert data["avg_rating"] is not None


def test_get_reviews(client):
    """GET /restaurants/<id>/reviews returns reviews for a restaurant."""
    response = client.get("/restaurants/1/reviews")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

    review = data[0]
    assert "author_name" in review
    assert "rating" in review
    assert "comment" in review
    assert review["restaurant_id"] == 1


def test_restaurant_not_found(client):
    """GET /restaurants/<id> returns 404 for non-existent restaurant."""
    response = client.get("/restaurants/9999")
    assert response.status_code == 404

    data = response.get_json()
    assert "error" in data


# ---------------------------------------------------------------------------
# The following tests SHOULD FAIL -- students must implement these features
# ---------------------------------------------------------------------------


def test_restaurant_stats(client):
    """GET /restaurants/<id>/stats returns rating statistics.

    SHOULD FAIL: This endpoint is not yet implemented.
    Students must add: average, total count, and rating distribution.
    """
    response = client.get("/restaurants/1/stats")
    assert response.status_code == 200

    data = response.get_json()
    assert "average" in data
    assert "total" in data
    assert "distribution" in data
    # distribution should map each star (1-5) to a count
    assert len(data["distribution"]) == 5


def test_create_review(client):
    """POST /restaurants/<id>/reviews creates a new review.

    SHOULD FAIL: This endpoint is not yet implemented.
    Students must add the POST handler and validate input.
    """
    payload = {
        "author_name": "Test User",
        "rating": 4,
        "comment": "Great place!",
    }
    response = client.post(
        "/restaurants/1/reviews",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert response.status_code == 201

    data = response.get_json()
    assert data["author_name"] == "Test User"
    assert data["rating"] == 4


def test_filter_by_cuisine(client):
    """GET /restaurants?cuisine=Japanese filters by cuisine.

    SHOULD FAIL: Query parameter filtering is not yet implemented.
    """
    response = client.get("/restaurants?cuisine=Japanese")
    assert response.status_code == 200

    data = response.get_json()
    assert len(data) == 1
    assert data[0]["cuisine"] == "Japanese"


def test_sort_restaurants(client):
    """GET /restaurants?sort=rating sorts by average rating descending.

    SHOULD FAIL: Query parameter sorting is not yet implemented.
    """
    response = client.get("/restaurants?sort=rating")
    assert response.status_code == 200

    data = response.get_json()
    ratings = [r["avg_rating"] for r in data]
    assert ratings == sorted(ratings, reverse=True)
