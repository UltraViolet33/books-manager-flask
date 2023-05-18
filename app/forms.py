from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, BooleanField, TextAreaField, SelectField, IntegerField, SelectMultipleField, PasswordField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[
                             DataRequired()], id="password")
    show_password = BooleanField('Show password', id='check')


class BookForm(FlaskForm):
    title = StringField("Titre", validators=[DataRequired()])
    image_link = StringField("Lien Image")
    summary = TextAreaField("Résumé")
    author = SelectField(validators=[DataRequired()])
    categories = SelectField(validators=[DataRequired()])


class AuthorForm(FlaskForm):
    name = StringField("Nom", validators=[DataRequired()])
    description = TextAreaField("Description")

class CategoryForm(FlaskForm):
    name = StringField("Nom", validators=[DataRequired()])
