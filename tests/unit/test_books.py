from app.forms import LoginForm


def test_all_books_route(test_client, init_database):
    test_client.get("/login")
    form = LoginForm(email="user1@gmail.com", password="User123!")

    response = test_client.post(
        "/login", data=form.data, follow_redirects=True)

    assert response.status_code == 200
    assert b"Logged in !" in response.data

    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Tous les livres" in response.data
    test_client.get("/logout")



def test_all_books_route_user_not_logged_in(test_client, init_database):
    response = test_client.get("/", follow_redirects=True)
    assert response.status_code == 200
    assert b"Se connecter" in response.data