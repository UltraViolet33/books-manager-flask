from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models.Book import Book
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import BookForm


books = Blueprint("books", __name__)


@books.route("/")
def home():
    books = Book.query.all()
    return render_template("index.html", user=current_user, books=books)


@books.route("/books/add", methods=["GET", "POST"])
@login_required
def add_book():

    form = BookForm()

    if form.validate_on_submit():
        book = Book(title=form.title.data, image_link=form.image_link.data)
        db.session.add(book)
        db.session.commit()

        return redirect(url_for("books.home"))

    return render_template("bookForm.html", user=current_user, form=form)
