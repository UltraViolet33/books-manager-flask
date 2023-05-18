from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models.Book import Book
from . import db


lists = Blueprint("lists", __name__)


@lists.route("/reading-list", methods=["GET"])
@login_required
def reading_list():
    books = current_user.reading_list
    return render_template("lists/reading_list.html", user=current_user, books=books)


@lists.route("/reading-list/add", methods=["POST"])
@login_required
def add_book_to_reading_list():
    book_id = request.form.get("book_id")
    book = Book.query.filter_by(id=book_id).first()
    current_user.reading_list.append(book)
    db.session.commit()

    flash("Book added to your reading list !", category="success")
    return redirect(url_for("books.details", id=book_id))


@lists.route("/reading-list/remove", methods=["POST"])
@login_required
def remove_book_from_reading_list():
    book_id = request.form.get("book_id")
    book = Book.query.filter_by(id=book_id).first()
    current_user.reading_list.remove(book)
    db.session.commit()

    flash("Book removed to your reading list !", category="success")
    return redirect(url_for("books.details", id=book_id))


@lists.route("/read-list", methods=["GET"])
@login_required
def read_list():
    books = current_user.read_list
    return render_template("lists/read_list.html", user=current_user, books=books)


@lists.route("/read-list/add", methods=["POST"])
@login_required
def add_book_to_read_list():
    book_id = request.form.get("book_id")
    book = Book.query.filter_by(id=book_id).first()
    current_user.read_list.append(book)
    db.session.commit()

    flash("Book added to your read list !", category="success")
    return redirect(url_for("books.details", id=book_id))


@lists.route("/read-list/remove", methods=["POST"])
@login_required
def remove_book_from_read_list():
    book_id = request.form.get("book_id")
    book = Book.query.filter_by(id=book_id).first()
    current_user.read_list.remove(book)
    db.session.commit()

    flash("Book removed to your read list !", category="success")
    return redirect(url_for("books.details", id=book_id))


@lists.route("/reading-in-progress-list", methods=["GET"])
@login_required
def reading_in_progress_list():
    books = current_user.reading_inprogress
    return render_template("lists/reading_in_progress_list.html", user=current_user, books=books)


@lists.route("/reading-in-progress-list/add", methods=["POST"])
@login_required
def add_book_to_reading_in_progress_list():
    book_id = request.form.get("book_id")
    book = Book.query.filter_by(id=book_id).first()
    current_user.reading_inprogress.append(book)
    db.session.commit()

    flash("Book added to your read list !", category="success")
    return redirect(url_for("books.details", id=book_id))


@lists.route("/reading-in-progress-list/remove", methods=["POST"])
@login_required
def remove_book_from_reading_in_progress_list():
    book_id = request.form.get("book_id")
    book = Book.query.filter_by(id=book_id).first()
    current_user.reading_inprogress.remove(book)
    db.session.commit()

    flash("Book removed to your read list !", category="success")
    return redirect(url_for("books.details", id=book_id))
