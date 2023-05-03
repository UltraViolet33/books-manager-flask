import re
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm import validates
from .. import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    image_link = db.Column(db.String(150), nullable=True)

    def __init__(self, title, image_link):
        self.title = title
        self.image_link = image_link
