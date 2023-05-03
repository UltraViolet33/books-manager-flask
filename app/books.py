from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models.User import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


books = Blueprint("books", __name__)


@books.route("/")
def home():
    return render_template("index.html", user=current_user)


@books.route("/books/add", methods=["GET", "POST"])
def add_book():


    return render_template("bookForm.html", user=current_user)