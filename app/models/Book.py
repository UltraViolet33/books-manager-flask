import re
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm import validates
from .. import db
from .Author import Author


books_authors_table = db.Table("books_authors",
                               db.Column("book_id", db.Integer,
                                         db.ForeignKey("books.id")),
                               db.Column("author_id", db.Integer,
                                         db.ForeignKey("authors.id"))
                               )


books_categories_table = db.Table("books_categories",
                                  db.Column("category_id", db.Integer,
                                            db.ForeignKey("categories.id")),
                                  db.Column("book_id", db.Integer,
                                            db.ForeignKey("books.id"))
                                  )


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    image_link = db.Column(db.String(150), nullable=True)
    summary = db.Column(db.String(500), nullable=True)

    authors = db.relationship(
        "Author", secondary=books_authors_table, backref="books")

    categories = db.relationship(
        "Category", secondary=books_categories_table, backref="books")

    def __init__(self, title, image_link, summary=""):
        self.title = title
        self.image_link = image_link
        self.summary = summary
