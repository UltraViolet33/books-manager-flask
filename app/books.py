from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models.Book import Book
from .models.Author import Author
from .models.Category import Category
from .forms import BookForm
from . import db


books = Blueprint("books", __name__)


@books.route("/")
@login_required
def home():
    books = Book.query.all()
    return render_template("index.html", user=current_user, books=books)


@books.route("/books/list")
@login_required
def list():
    books = Book.query.all()
    return render_template("books/list.html", user=current_user, books=books)


@books.route("/books/<id>")
@login_required
def details(id):
    book = Book.get_single_book(id, current_user)
    return render_template("books/details.html", user=current_user, book=book)


@books.route("/books/edit/<id>", methods=["GET", "POST"])
@login_required
def edit_book(id):
    form = BookForm()
    form.author.choices = [(c.id, c.name) for c in Author.query.all()]
    form.categories.choices = [(c.id, c.name) for c in Category.query.all()]
    book = Book.get_single_book(id, current_user)

    if request.method == "GET":
        form.summary.data = book.summary 

    if request.method == "POST" and form.validate_on_submit():
        print("ok")
        book.title = form.title.data
        book.image_link = form.image_link.data
        book.summary = form.summary.data
        author = Author.query.filter_by(id=form.author.data).first()

        category = Category.query.filter_by(id=form.categories.data).first()
        book.authors = []
        books.categories = []
        book.authors.append(author)
        book.categories.append(category)
        db.session.commit()

        flash(f"{book.title} a été modifier !", category="success")
        return redirect(url_for("books.list"))


    return render_template("books/book_form.html", form=form, user=current_user, book=book)


@books.route("/books/add", methods=["GET", "POST"])
@login_required
def add_book():
    form = BookForm()
    form.author.choices = [(c.id, c.name) for c in Author.query.all()]
    form.categories.choices = [(c.id, c.name) for c in Category.query.all()]

    if form.validate_on_submit():

        book = Book(title=form.title.data,
                    image_link=form.image_link.data, summary=form.summary.data)
        author = Author.query.filter_by(id=form.author.data).first()

        category = Category.query.filter_by(id=form.categories.data).first()

        book.authors.append(author)
        book.categories.append(category)
        db.session.add(book)
        db.session.commit()

        return redirect(url_for("books.home"))

    return render_template("books/book_form.html", user=current_user, form=form)
