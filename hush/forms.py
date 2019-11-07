from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, RadioField, BooleanField, PasswordField, SubmitField, TextAreaField, \
    SelectField, HiddenField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, Required, NumberRange, ValidationError


class flags(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField('Done')
