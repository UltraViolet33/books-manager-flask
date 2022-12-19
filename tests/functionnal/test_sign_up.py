from website import create_app


def test_sign_up_route():

    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get("/signup")
        assert response.status_code == 200
