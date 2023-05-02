from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models.User import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if user.is_password_correct(password):
                flash("Logged in !", category="success")
                login_user(user, remember=True)
                return render_template("index.html", user=current_user)
            else:
                flash("Email or password incorrect !", category="error")
        else:
            print(email)
            flash("Email or password incorrect !", category="error")

    return render_template("login.html", user=current_user)
