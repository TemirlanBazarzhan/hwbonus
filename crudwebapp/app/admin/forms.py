# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired

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

class DiscoverForm(FlaskForm):
    cname = StringField('Country Name', validators=[DataRequired()])
    disease_code = StringField('Disease Code', validators=[DataRequired()])
    first_enc_date = DateField('First Enc Date', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PublicServantForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    department = StringField('Deparment', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DoctorForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    degree = StringField('degree', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SpecializeForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RecordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    cname = StringField('Country Name', validators=[DataRequired()])
    disease_code = StringField('Disease Code', validators=[DataRequired()])
    total_deaths = IntegerField('Total Deaths', validators =[DataRequired()])
    total_patients = IntegerField('Total Patients', validators=[DataRequired()])
    submit = SubmitField('Submit')