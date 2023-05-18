from . import db
from flask import Blueprint, render_template, redirect, url_for, request
from .models.Category import Category
from .forms import CategoryForm
from flask_login import login_required, current_user

categories = Blueprint("categories", __name__)


@categories.route("/add", methods=["GET", "POST"])
@login_required
def add_category():

    form = CategoryForm()

    if request.method == "POST":
        if form.validate_on_submit():
            category_name = form.name.data
            # check if name already exists
            category = Category(name=category_name)
            db.session.add(category)
            db.session.commit()

        return redirect(url_for("books.home"))

    return render_template("categories/add_category.html", user=current_user, form=form)


@categories.route("/all")
@login_required
def all_categories():
    categories = Category.query.all()
    return render_template("categories/all_categories.html", categories=categories, user=current_user)
