from flask import url_for
from app import create_app
from flask_login import current_user
from app.forms import LoginForm


def test_all_categories_route(test_client, init_database):
    test_client.get("/login")
    form = LoginForm(email="user1@gmail.com", password="User123!")

    response = test_client.post(
        "/login", data=form.data, follow_redirects=True)

    assert response.status_code == 200
    assert b"Logged in !" in response.data

    response = test_client.get("/categories/all")
    assert response.status_code == 200
    assert b"All categories" in response.data
