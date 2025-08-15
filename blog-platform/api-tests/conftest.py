import pytest
import requests
import time
from typing import Dict, Any

""" Not every function will be called when a test run, only being run when the function is called """
@pytest.fixture(scope="session")
def base_url():
    """ Base URL for the API """
    return "http://localhost:9090/api/v1"


@pytest.fixture(scope="session")
def auth_token(base_url):
    """ Get authentication token by registering a new test user every test"""
    # Register a test user
    user_data = {
        # {} - f-string placeholder to insert the value
        "email": f"test-{int(time.time())}@example.com",
        "password": "password123456"
    }

    response = requests.post(f"{base_url}/auth/register", json=user_data)
    # If the assertion fails, it displays a custom error message: f"Failed to register user: {response.text}"
    assert response.status_code == 200, f"Failed to register a test user: {response.text}"


@pytest.fixture(scope="session")
def test_data(base_url, auth_token):
    """ Create the test data (catagory and tags) for test """
    headers = {"Authorization": f"Bearer {auth_token}"}

    # Create test catagory
    category_data = {"name": f"Test Category {int(time.time())}"}
    category_response = requests.post(f"{base_url}/categories", json=category_data, headers=headers)
    assert category_response.status_code == 201, f"Failed to create category: {category_response.text}"
    category_id = category_response.json()["id"]

    # Create test tags
    tags_data = {"names": [f"Test Tag {int(time.time())}", f"Test Tag {int(time.time()) + 1}"]}
    tags_response = requests.post(f"{base_url}/tags", json=tags_data, headers=headers)
    assert tags_response.status_code == 201, f"Failed to create tags: {tags_response.text}"
    tag_ids = [tag["id"] for tag in tags_response.json()]

    return {
        "category_id": category_id,
        "tag_ids": tag_ids,
        "headers": headers
    }


@pytest.fixture(scope="function")
def clean_test_data(base_url, auth_token, test_data):
    """ Clean the data that fixture created after each test """
    yield # This runs the test

    # Cleanup: Delete test posts ( if any were created )
    headers = {"Authorization": f"Bearer {auth_token}"}
    posts_response = requests.get(f"{base_url}/posts", headers=headers)
    if posts_response.status_code == 200:
        posts = posts_response.json()
        for post in posts:
            if "Test Post" in post.get("title", ""):
                requests.delete(f"{base_url}/posts/{post['id']}", headers=headers)


def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "auth: marks tests as authentication tests"
    )
        














