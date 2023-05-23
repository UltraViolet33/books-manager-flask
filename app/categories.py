from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models.Category import Category
from .forms import CategoryForm
from . import db


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

            flash(f"Catégorie {category.name} ajouté", category="success")
            return redirect(url_for("categories.all_categories"))

    return render_template("categories/category_form.html", user=current_user, form=form)


@categories.route("/edit/<id>", methods=["GET", "POST"])
@login_required
def edit_category(id):
    category = Category.query.filter_by(id=id).first()

    if not category:
        return "404", 404

    form = CategoryForm()

    if request.method == "GET":
        form.name.data = category.name


    if request.method == "POST":
        if form.validate_on_submit():
            category.name = form.name.data
            # check if name already exists
            db.session.commit()

            flash(f"Catégorie {category.name} modifiée", category="success")
            return redirect(url_for("categories.all_categories"))

    return render_template("categories/category_form.html", user=current_user, category=category, form=form)


@categories.route("/all")
@login_required
def all_categories():
    categories = Category.query.all()
    return render_template("categories/all_categories.html", categories=categories, user=current_user)
