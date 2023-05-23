from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models.Author import Author
from .forms import AuthorForm
from . import db


authors = Blueprint("authors", __name__)


@authors.route("/add", methods=["GET", "POST"])
@login_required
def add_author():
    form = AuthorForm()

    if form.validate_on_submit():
        # check if author already exists
        author = Author(name=form.name.data, description=form.description.data)
        db.session.add(author)
        db.session.commit()

        flash(f"Auteur {author.name} ajouté", category="success")
        return redirect(url_for("authors.all_authors"))

    return render_template("authors/author_form.html", user=current_user, form=form)


@authors.route("/edit/<id>", methods=["GET", "POST"])
@login_required
def edit_author(id):
    author = Author.query.filter_by(id=id).first()

    if not author:
        return "404", 404

    form = AuthorForm()

    if request.method == "GET":
        form.name.data = author.name
        form.description.data = author.description

    if form.validate_on_submit():
        # check if author already exists
        author.name = form.name.data
        author.description = form.description.data

        db.session.commit()

        flash(f"Auteur {author.name} modifié", category="success")
        return redirect(url_for("authors.all_authors"))

    return render_template("authors/author_form.html", author=author, user=current_user, form=form)


@authors.route("/all")
@login_required
def all_authors():
    all_authors = Author.query.all()
    return render_template("authors/all_authors.html", user=current_user, authors=all_authors)
