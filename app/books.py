from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models.Book import Book
from .models.Author import Author
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import BookForm


books = Blueprint("books", __name__)


@books.route("/")
def home():
    books = Book.query.all()


    for book in books:
        book.is_in_reading_list = False
        for user in book.users_reading_list:
            if user.id == current_user.id:
                book.is_in_reading_list = True

    return render_template("index.html", user=current_user, books=books)


@books.route("/books/add", methods=["GET", "POST"])
@login_required
def add_book():

    form = BookForm()
    form.author.choices = [(c.id, c.name) for c in Author.query.all()]


    if form.validate_on_submit():

        book = Book(title=form.title.data, image_link=form.image_link.data)
        author = Author.query.filter_by(id=form.author.data).first()

        book.authors.append(author)
        db.session.add(book)
        db.session.commit()

        return redirect(url_for("books.home"))

    return render_template("bookForm.html", user=current_user, form=form)



@books.route("/books/reading-list/add/<id>", methods=["GET"])
@login_required
def add_book_to_reading_list(id):
    book = Book.query.filter_by(id=id).first()

    current_user.reading_list.append(book)
    db.session.commit()

    return redirect(url_for("books.home"))