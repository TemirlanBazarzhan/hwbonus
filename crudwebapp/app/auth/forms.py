# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import *

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    cname = StringField('Country Name', validators = [DataRequired()])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Users.query.filter_by(phone=field.data).first():
            raise ValidationError('Phone is already in use.')

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class DiseaseTypeForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CountryForm(FlaskForm):
    cname = StringField('Country Name', validators=[DataRequired()])
    population = IntegerField('Population', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DiseaseForm(FlaskForm):
    disease_code = StringField('Disease Code', validators=[DataRequired()])
    pathogen = StringField('Pathogen', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    id = IntegerField('Id', validators=[DataRequired()])
    submit = SubmitField('Submit')