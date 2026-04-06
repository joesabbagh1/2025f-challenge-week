"""Pytest fixtures for Study Flashcards API tests."""

import os
import sys
import pytest
import mysql.connector
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

TEST_DB_NAME = "test_study_flashcards"


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Create and seed the test database once before all tests."""
    import database
    from seed import seed

    # Create the test database
    config_no_db = {k: v for k, v in database.DB_CONFIG.items() if k != "database"}
    conn = mysql.connector.connect(**config_no_db)
    cursor = conn.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS {TEST_DB_NAME}")
    cursor.execute(f"CREATE DATABASE {TEST_DB_NAME}")
    cursor.close()
    conn.close()

    database.DB_CONFIG["database"] = TEST_DB_NAME
    seed(TEST_DB_NAME)
    yield

    # Cleanup
    conn = mysql.connector.connect(**config_no_db)
    cursor = conn.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS {TEST_DB_NAME}")
    cursor.close()
    conn.close()


@pytest.fixture()
def client():
    """Return a FastAPI TestClient."""
    from app import app
    return TestClient(app)
