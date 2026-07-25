import os

os.environ.setdefault("DB_CONNECTION", "sqlite:///./test.db")
os.environ.setdefault("SECRET_KEY", "test-secret")
os.environ.setdefault("ALGORITHM", "HS256")
os.environ.setdefault("EXP_TIME", "30")

from main import app


def test_restful_task_and_user_routes_are_registered():
    registered_paths = {route.path for route in app.routes}

    assert "/tasks" in registered_paths
    assert "/tasks/{task_id}" in registered_paths
    assert "/users/register" in registered_paths
    assert "/users/login" in registered_paths
    assert "/users/me" in registered_paths
