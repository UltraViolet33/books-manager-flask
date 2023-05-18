from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models.User import User
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit() or request.form.get("email"):
            email = request.form.get("email")
            password = request.form.get("password")

            user = User.query.filter_by(email=email).first()
            if user:
                if user.is_password_correct(password):
                    flash("Logged in !", category="success")
                    login_user(user, remember=True)
                    return redirect("/")

                flash("Invalid email or password", category="error")

    return render_template("login.html", user=current_user, form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")
