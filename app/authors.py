from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models.Author import Author
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import AuthorForm


authors = Blueprint("authors", __name__)


@authors.route("/add", methods=["GET", "POST"])
@login_required
def add_author():

    form = AuthorForm()

    if form.validate_on_submit():
        #check if author already exists
        author = Author(name=form.name.data, description=form.description.data)
        db.session.add(author)
        db.session.commit()

        flash(f"Auteur {author.name} ajouté", category="success")
        return redirect(url_for("authors.all_authors"))

    return render_template("authors/add_author.html", user=current_user, form=form)


@authors.route("/all")
@login_required
def all_authors():
    all_authors = Author.query.all()
    return render_template("authors/all_authors.html", user=current_user, authors=all_authors)
