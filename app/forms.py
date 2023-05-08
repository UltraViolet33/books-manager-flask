from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField("Titre", validators=[DataRequired()])
    image_link = StringField("Lien Image")
    author = SelectField(validators=[DataRequired()])
    categories = SelectField(validators=[DataRequired()])



class AuthorForm(FlaskForm):
    name = StringField("Nom", validators=[DataRequired()])


class CategoryForm(FlaskForm):
    name = StringField("Nom", validators=[DataRequired()])