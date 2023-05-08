from flask import url_for
import json
from app import create_app
from flask_login import current_user



def test_login_route(test_client):
    response = test_client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data



def test_login_form(test_client):

    response = test_client.post("/login", data={
        "email": "user1@gmail.com",
        "password": "User123!"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Logged in !" in response.data
    # assert b"Logout" in response.get_data(as_text=True)