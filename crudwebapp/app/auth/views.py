# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import *
from .. import db
from ..models import Users

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(email=form.email.data,
                            phone=form.phone.data,
                            name=form.name.data,
                            surname=form.surname.data,
                            cname=form.cname.data,
                            password=form.password.data)

        # add employee to the database
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        
        user = Users.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            
            if user.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))
           

        
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))

@auth.route('/diseasetypes', methods=['GET', 'POST'])
@login_required
def list_diseasetypes():


    diseasetypes = DiseaseType.query.all()

    return render_template('auth/diseasetypes/diseasetypes.html',
                           diseasetypes=diseasetypes, title="Disease Types")

@auth.route('/diseasetypes/add', methods=['GET', 'POST'])
@login_required
def add_diseasetype():
    

    add_diseasetype = True

    form = DiseaseTypeForm()
    if form.validate_on_submit():
        diseasetype = DiseaseType(id=form.id.data,
                                description=form.description.data)
        try:
            db.session.add(diseasetype)
            db.session.commit()
            flash('You have successfully added a new disease type.')
        except:
            flash('Error: disease type id already exists.')

        # redirect to departments page
        return redirect(url_for('auth.list_diseasetypes'))

    # load department template
    return render_template('auth/diseasetypes/diseasetype.html', action="Add",
                           add_diseasetype=add_diseasetype, form=form,
                           title="Add Disease Type")

@auth.route('/diseasetype/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_diseasetype(id):
    

    add_diseasetype = False

    diseasetype = DiseaseType.query.get_or_404(id)
    form = DiseaseTypeForm(obj=diseasetype)
    if form.validate_on_submit():
        diseasetype.id = form.id.data
        diseasetype.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the diseasetype.')

        # redirect to the departments page
        return redirect(url_for('auth.list_diseasetypes'))

    form.description.data = diseasetype.description
    form.id.data = diseasetype.id
    return render_template('auth/diseasetypes/diseasetype.html', action="Edit",
                           add_diseasetype=add_diseasetype, form=form,
                           diseasetype=diseasetype, title="Edit Disease Type")

@auth.route('/diseasetypes/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_diseasetype(id):
    

    diseasetype = DiseaseType.query.get_or_404(id)
    db.session.delete(diseasetype)
    db.session.commit()
    flash('You have successfully deleted the disease type.')

    # redirect to the departments page
    return redirect(url_for('auth.list_diseasetypes'))

    return render_template(title="Delete Disease Type")



@auth.route('/countries')
@login_required
def list_countries():
    countries = Country.query.all()
    return render_template('auth/countries/countries.html',
                           countries=countries, title='Countries')

@auth.route('/countries/add', methods=['GET', 'POST'])
@login_required
def add_country():
    add_country = True

    form = CountryForm()
    if form.validate_on_submit():
        country = Country(cname=form.cname.data,
                    population=form.population.data)

        try:
            db.session.add(country)
            db.session.commit()
            flash('You have successfully added a new country.')
        except:
            flash('Error: country name already exists.')

       
        return redirect(url_for('auth.list_countries'))

   
    return render_template('auth/countries/country.html', action="Add", add_country=add_country,
                           form=form, title='Add Country')

@auth.route('/countries/edit/<string:cname>', methods=['GET', 'POST'])
@login_required
def edit_country(cname):
   

    add_country = False

    country = Country.query.get_or_404(cname)
    form = CountryForm(obj=country)
    if form.validate_on_submit():
        country.cname = form.cname.data
        country.population = form.population.data
        db.session.add(country)
        db.session.commit()
        flash('You have successfully edited the country.')

        
        return redirect(url_for('auth.list_countries'))

    form.population.data = country.population
    form.cname.data = country.cname
    return render_template('auth/countries/country.html', add_country=add_country,
                           form=form, title="Edit Country")

@auth.route('/countries/delete/<string:cname>', methods=['GET', 'POST'])
@login_required
def delete_country(cname):
    

    country = Country.query.get_or_404(cname)
    db.session.delete(country)
    db.session.commit()
    flash('You have successfully deleted the country.')

    
    return redirect(url_for('auth.list_countries'))

    return render_template(title="Delete Country")


@auth.route('/diseases', methods=['GET', 'POST'])
@login_required
def list_diseases():
    

    diseases = Disease.query.all()

    return render_template('auth/diseases/diseases.html',
                           diseases=diseases, title="Diseases")

@auth.route('/diseases/add', methods=['GET', 'POST'])
@login_required
def add_disease():
    

    add_disease = True

    form = DiseaseForm()
    if form.validate_on_submit():
        disease = Disease(disease_code=form.disease_code.data,
                                pathogen=form.pathogen.data,
                                description=form.description.data,
                                id=form.id.data)
        try:
            db.session.add(disease)
            db.session.commit()
            flash('You have successfully added a new disease.')
        except:
            flash('Error: disease code already exists.')

        # redirect to departments page
        return redirect(url_for('auth.list_diseases'))

    # load department template
    return render_template('auth/diseases/disease.html', action="Add",
                           add_disease=add_disease, form=form,
                           title="Add Disease")

@auth.route('/disease/edit/<string:disease_code>', methods=['GET', 'POST'])
@login_required
def edit_disease(disease_code):
    

    add_disease = False

    disease = Disease.query.get_or_404(disease_code)
    form = DiseaseForm(obj=disease)
    if form.validate_on_submit():
        disease.disease_code = form.disease_code.data
        disease.pathogen = form.pathogen.data
        disease.description = form.description.data
        disease.id = form.id.data
        db.session.commit()
        flash('You have successfully edited the disease.')

        # redirect to the departments page
        return redirect(url_for('auth.list_diseases'))

    form.id.data = disease.id
    form.description.data = disease.description
    form.pathogen = disease.pathogen
    form.disease_code = disease.disease_code
    return render_template('auth/diseases/disease.html', action="Edit",
                           add_disease=add_disease, form=form,
                           disease=disease, title="Edit Disease")

@auth.route('/diseases/delete/<string:disease_code>', methods=['GET', 'POST'])
@login_required
def delete_disease(disease_code):
    

    disease = Disease.query.get_or_404(disease_code)
    db.session.delete(disease)
    db.session.commit()
    flash('You have successfully deleted the disease.')

    # redirect to the departments page
    return redirect(url_for('auth.list_diseases'))

    return render_template(title="Delete Disease")


