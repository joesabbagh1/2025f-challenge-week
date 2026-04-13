import os
import sys
import pytest
import mysql.connector

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import database
from app import app as flask_app
from seed import RESTAURANTS, REVIEWS

TEST_DB_NAME = "test_campus_food_guide"


@pytest.fixture
def app(tmp_path):
    """Create a test app with a temporary MySQL database."""
    # Create test database
    config_no_db = {k: v for k, v in database.DB_CONFIG.items() if k != "database"}
    conn = mysql.connector.connect(**config_no_db)
    cursor = conn.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS {TEST_DB_NAME}")
    cursor.execute(f"CREATE DATABASE {TEST_DB_NAME}")
    cursor.close()
    conn.close()

    database.DB_CONFIG["database"] = TEST_DB_NAME
    database.init_db()

    # Seed test data
    db = database.get_db()
    cursor = db.cursor()
    cursor.executemany(
        "INSERT INTO restaurants (name, cuisine, address, price_range, image_url) VALUES (%s, %s, %s, %s, %s)",
        RESTAURANTS,
    )
    cursor.executemany(
        "INSERT INTO reviews (restaurant_id, author_name, rating, comment) VALUES (%s, %s, %s, %s)",
        REVIEWS,
    )
    db.commit()
    cursor.close()
    db.close()

    flask_app.config["TESTING"] = True
    yield flask_app

    # Cleanup
    conn = mysql.connector.connect(**config_no_db)
    cursor = conn.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS {TEST_DB_NAME}")
    cursor.close()
    conn.close()


@pytest.fixture
def client(app):
    """Return a test client for the Flask app."""
    return app.test_client()
