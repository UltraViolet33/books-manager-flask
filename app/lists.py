from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from .models.Book import Book
from .models.Author import Author
from .models.Category import Category
from .forms import BookForm
from . import db


lists = Blueprint("lists", __name__)

@lists.route("/reading-list", methods=["GET"])
@login_required
def reading_list():
    books = current_user.reading_list
    return render_template("lists/reading_list.html", user=current_user, books=books)





@lists.route("/read-list", methods=["GET"])
@login_required
def read_list():
    books = current_user.read_list
    return render_template("read_list.html", user=current_user, books=books)