from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField("Titre", validators=[DataRequired()])
    image_link = StringField("Lien Image")
