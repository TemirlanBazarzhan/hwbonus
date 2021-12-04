# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import *
from .. import db
from ..models import *

def check_admin():
    if not current_user.is_admin:
        abort(403)



@admin.route('/diseasetypes', methods=['GET', 'POST'])
@login_required
def list_diseasetypes():
    check_admin()

    diseasetypes = DiseaseType.query.all()

    return render_template('admin/diseasetypes/diseasetypes.html',
                           diseasetypes=diseasetypes, title="Disease Types")

@admin.route('/diseasetypes/add', methods=['GET', 'POST'])
@login_required
def add_diseasetype():
    check_admin()

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
        return redirect(url_for('admin.list_diseasetypes'))

    # load department template
    return render_template('admin/diseasetypes/diseasetype.html', action="Add",
                           add_diseasetype=add_diseasetype, form=form,
                           title="Add Disease Type")

@admin.route('/diseasetype/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_diseasetype(id):
    check_admin()

    add_diseasetype = False

    diseasetype = DiseaseType.query.get_or_404(id)
    form = DiseaseTypeForm(obj=diseasetype)
    if form.validate_on_submit():
        diseasetype.id = form.id.data
        diseasetype.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the diseasetype.')

        # redirect to the departments page
        return redirect(url_for('admin.list_diseasetypes'))

    form.description.data = diseasetype.description
    form.id.data = diseasetype.id
    return render_template('admin/diseasetypes/diseasetype.html', action="Edit",
                           add_diseasetype=add_diseasetype, form=form,
                           diseasetype=diseasetype, title="Edit Disease Type")

@admin.route('/diseasetypes/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_diseasetype(id):
    check_admin()

    diseasetype = DiseaseType.query.get_or_404(id)
    db.session.delete(diseasetype)
    db.session.commit()
    flash('You have successfully deleted the disease type.')

    # redirect to the departments page
    return redirect(url_for('admin.list_diseasetypes'))

    return render_template(title="Delete Disease Type")



@admin.route('/countries')
@login_required
def list_countries():
    check_admin()
    countries = Country.query.all()
    return render_template('admin/countries/countries.html',
                           countries=countries, title='Countries')

@admin.route('/countries/add', methods=['GET', 'POST'])
@login_required
def add_country():
    check_admin()

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

       
        return redirect(url_for('admin.list_countries'))

   
    return render_template('admin/countries/country.html', action="Add", add_country=add_country,
                           form=form, title='Add Country')

@admin.route('/countries/edit/<string:cname>', methods=['GET', 'POST'])
@login_required
def edit_country(cname):
   
    check_admin()

    add_country = False

    country = Country.query.get_or_404(cname)
    form = CountryForm(obj=country)
    if form.validate_on_submit():
        country.cname = form.cname.data
        country.population = form.population.data
        db.session.add(country)
        db.session.commit()
        flash('You have successfully edited the country.')

        
        return redirect(url_for('admin.list_countries'))

    form.population.data = country.population
    form.cname.data = country.cname
    return render_template('admin/countries/country.html', add_country=add_country,
                           form=form, title="Edit Country")

@admin.route('/countries/delete/<string:cname>', methods=['GET', 'POST'])
@login_required
def delete_country(cname):
    check_admin()

    country = Country.query.get_or_404(cname)
    db.session.delete(country)
    db.session.commit()
    flash('You have successfully deleted the country.')

    
    return redirect(url_for('admin.list_countries'))

    return render_template(title="Delete Country")


@admin.route('/diseases', methods=['GET', 'POST'])
@login_required
def list_diseases():
    check_admin()

    diseases = Disease.query.all()

    return render_template('admin/diseases/diseases.html',
                           diseases=diseases, title="Diseases")

@admin.route('/diseases/add', methods=['GET', 'POST'])
@login_required
def add_disease():
    check_admin()

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
        return redirect(url_for('admin.list_diseases'))

    # load department template
    return render_template('admin/diseases/disease.html', action="Add",
                           add_disease=add_disease, form=form,
                           title="Add Disease")

@admin.route('/disease/edit/<string:disease_code>', methods=['GET', 'POST'])
@login_required
def edit_disease(disease_code):
    check_admin()

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
        return redirect(url_for('admin.list_diseases'))

    form.id.data = disease.id
    form.description.data = disease.description
    form.pathogen = disease.pathogen
    form.disease_code = disease.disease_code
    return render_template('admin/diseases/disease.html', action="Edit",
                           add_disease=add_disease, form=form,
                           disease=disease, title="Edit Disease")

@admin.route('/diseases/delete/<string:disease_code>', methods=['GET', 'POST'])
@login_required
def delete_disease(disease_code):
    check_admin()

    disease = Disease.query.get_or_404(disease_code)
    db.session.delete(disease)
    db.session.commit()
    flash('You have successfully deleted the disease.')

    # redirect to the departments page
    return redirect(url_for('admin.list_diseases'))

    return render_template(title="Delete Disease")


@admin.route('/discovers', methods=['GET', 'POST'])
@login_required
def list_discovers():
    check_admin()

    discovers = Discover.query.all()

    return render_template('admin/discovers/discovers.html',
                           discovers=discovers, title="Discovers")



@admin.route('/discovers/add', methods=['GET', 'POST'])
@login_required
def add_discover():
    check_admin()

    add_discover = True

    form = DiscoverForm()
    if form.validate_on_submit():
        discover = Discover(cname=form.cname.data,
                                disease_code=form.disease_code.data,
                                first_enc_date=form.first_enc_date.data)
        try:
            db.session.add(discover)
            db.session.commit()
            flash('You have successfully added a new discover.')
        except:
            flash('Error: discover instance already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_discovers'))

    # load department template
    return render_template('admin/discovers/discover.html', action="Add",
                           add_discover=add_discover, form=form,
                           title="Add Discover")

@admin.route('/discover/edit/<string:cname>/<string:disease_code>', methods=['GET', 'POST'])
@login_required
def edit_discover(cname, disease_code):
    check_admin()

    add_discover = False

    discover = Discover.query.get_or_404(cname, disease_code)
    form = DiscoverForm(obj=discover)
    if form.validate_on_submit():
        discover.cname = form.cname.data
        discover.disease_code = form.disease_code.data
        discover.first_enc_date = form.first_enc_date.data
        db.session.commit()
        flash('You have successfully edited the discover instance.')

        # redirect to the departments page
        return redirect(url_for('admin.list_discovers'))

    form.first_enc_date.data = discover.first_enc_date
    form.disease_code.data = discover.disease_code
    form.cname = discover.cname
    return render_template('admin/discovers/discover.html', action="Edit",
                           add_discover=add_discover, form=form,
                           discover=discover, title="Edit Discover")

@admin.route('/discovers/delete/<string:cname>/<string:disease_code>', methods=['GET', 'POST'])
@login_required
def delete_discover(cname, disease_code):
    check_admin()

    discover = Disease.query.get_or_404(cname, disease_code)
    db.session.delete(discover)
    db.session.commit()
    flash('You have successfully deleted the discover instance.')

    
    return redirect(url_for('admin.list_discovers'))

    return render_template(title="Delete Discover")


@admin.route('/publicservants', methods=['GET', 'POST'])
@login_required
def list_publicservants():
    check_admin()

    publicservants = PublicServant.query.all()

    return render_template('admin/publicservants/publicservants.html',
                           publicservants=publicservants, title="Public Servants")



@admin.route('/publicservants/add', methods=['GET', 'POST'])
@login_required
def add_publicservant():
    check_admin()

    add_publicservant = True

    form = PublicServantForm()
    if form.validate_on_submit():
        publicservant = PublicServant(email=form.email.data,
                                department=form.department.data)
        try:
            db.session.add(publicservant)
            db.session.commit()
            flash('You have successfully added a new public servant.')
        except:
            flash('Error: public servant already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_publicservants'))

    # load department template
    return render_template('admin/publicservants/publicservant.html', action="Add",
                           add_publicservant=add_publicservant, form=form,
                           title="Add Public Servant")

@admin.route('/publicservant/edit/<string:email>', methods=['GET', 'POST'])
@login_required
def edit_publicservant(email):
    check_admin()

    add_publicservant = False

    publicservant = PublicServant.query.get_or_404(email)
    form = PublicServantForm(obj=publicservant)
    if form.validate_on_submit():
        publicservant.email = form.email.data
        publicservant.department = form.department.data
        db.session.commit()
        flash('You have successfully edited the public servant.')

        # redirect to the departments page
        return redirect(url_for('admin.list_publicservants'))

    form.department.data = publicservant.department
    form.email.data = publicservant.email

    return render_template('admin/publicservants/publicservant.html', action="Edit",
                           add_publicservant=add_publicservant, form=form,
                           publicservant=publicservant, title="Edit Public Servant")

@admin.route('/publicservants/delete/<string:email>', methods=['GET', 'POST'])
@login_required
def delete_publicservant(email):
    check_admin()

    publicservant = PublicServant.query.get_or_404(email)
    db.session.delete(publicservant)
    db.session.commit()
    flash('You have successfully deleted the public servant.')

    
    return redirect(url_for('admin.list_publicservants'))

    return render_template(title="Delete Public Servant")


@admin.route('/doctors', methods=['GET', 'POST'])
@login_required
def list_doctors():
    check_admin()

    doctors = Doctor.query.all()

    return render_template('admin/doctors/doctors.html',
                           doctors=doctors, title="Doctors")



@admin.route('/doctors/add', methods=['GET', 'POST'])
@login_required
def add_doctor():
    check_admin()

    add_doctor = True

    form = DoctorForm()
    if form.validate_on_submit():
        doctor = Doctor(email=form.email.data,
                                degree=form.degree.data)
        try:
            db.session.add(doctor)
            db.session.commit()
            flash('You have successfully added a new doctor.')
        except:
            flash('Error: doctor already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_doctors'))

    # load department template
    return render_template('admin/doctors/doctor.html', action="Add",
                           add_doctor=add_doctor, form=form,
                           title="Add Doctor")

@admin.route('/doctor/edit/<string:email>', methods=['GET', 'POST'])
@login_required
def edit_doctor(email):
    check_admin()

    add_doctor = False

    doctor = Doctor.query.get_or_404(email)
    form = DoctorForm(obj=doctor)
    if form.validate_on_submit():
        doctor.email = form.email.data
        doctor.degree = form.degree.data
        db.session.commit()
        flash('You have successfully edited the doctor.')

        # redirect to the departments page
        return redirect(url_for('admin.list_doctors'))

    form.degree.data = doctor.degree
    form.email.data = doctor.email

    return render_template('admin/doctors/doctor.html', action="Edit",
                           add_doctor=add_doctor, form=form,
                           doctor=doctor, title="Edit Doctor")

@admin.route('/doctors/delete/<string:email>', methods=['GET', 'POST'])
@login_required
def delete_doctor(email):
    check_admin()

    doctor = Doctor.query.get_or_404(email)
    db.session.delete(doctor)
    db.session.commit()
    flash('You have successfully deleted the doctor.')

    
    return redirect(url_for('admin.list_doctors'))

    return render_template(title="Delete Doctor")


@admin.route('/specialize', methods=['GET', 'POST'])
@login_required
def list_specialize():
    check_admin()

    specializes = Specialize.query.all()

    return render_template('admin/specializes/specializes.html',
                           specializes=specializes, title="Specializes")



@admin.route('/specializes/add', methods=['GET', 'POST'])
@login_required
def add_specialize():
    check_admin()

    add_specialize = True

    form = SpecializeForm()
    if form.validate_on_submit():
        specialize = Specialize(id=form.id.data,
                                email=form.email.data)
        try:
            db.session.add(specialize)
            db.session.commit()
            flash('You have successfully added a new specialization.')
        except:
            flash('Error: specialization already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_specializes'))

    # load department template
    return render_template('admin/specializes/specialize.html', action="Add",
                           add_specialize=add_specialize, form=form,
                           title="Add Specialize")

@admin.route('/specialize/edit/<int:id>/<string:email>', methods=['GET', 'POST'])
@login_required
def edit_specialize(id, email):
    check_admin()

    add_specialize = False

    specialize = Specialize.query.get_or_404(id, email)
    form = SpecializeForm(obj=specialize)
    if form.validate_on_submit():
        specialize.id = form.id.data
        specialize.email = form.email.data
        db.session.commit()
        flash('You have successfully edited the specialization.')

        # redirect to the departments page
        return redirect(url_for('admin.list_specializes'))

    form.email.data = specialize.email
    form.id.data = specialize.id

    return render_template('admin/specializes/specialize.html', action="Edit",
                           add_specialize=add_specialize, form=form,
                           specialize=specialize, title="Edit Specialize")

@admin.route('/specializes/delete/<int:id>/<string:email>', methods=['GET', 'POST'])
@login_required
def delete_specialize(id, email):
    check_admin()

    specialize = Specialize.query.get_or_404(id, email)
    db.session.delete(specialize)
    db.session.commit()
    flash('You have successfully deleted the specialization.')

    
    return redirect(url_for('admin.list_specializes'))

    return render_template(title="Delete Specialize")



@admin.route('/records', methods=['GET', 'POST'])
@login_required
def list_records():
    check_admin()

    records = Record.query.all()

    return render_template('admin/records/records.html',
                           records=records, title="Records")



@admin.route('/records/add', methods=['GET', 'POST'])
@login_required
def add_record():
    check_admin()

    add_record = True

    form = RecordForm()
    if form.validate_on_submit():
        record = Record(email=form.email.data,
                                cname=form.cname.data,
                                disease_code=form.disease_code.data,
                                total_deaths=form.total_deaths.data,
                                total_patients=form.total_patients.data)
        try:
            db.session.add(record)
            db.session.commit()
            flash('You have successfully added a new record.')
        except:
            flash('Error: record already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_records'))

    # load department template
    return render_template('admin/records/record.html', action="Add",
                           add_record=add_record, form=form,
                           title="Add Record")

@admin.route('/record/edit/<string:email>/<string:cname>/<string:disease_code>', methods=['GET', 'POST'])
@login_required
def edit_record(email, cname, disease_code):
    check_admin()

    add_record = False

    record = Record.query.get_or_404(email, cname, disease_code)
    form = RecordForm(obj=record)
    if form.validate_on_submit():
        record.email = form.email.data
        record.cname = form.cname.data
        record.disease_code = form.disease_code.data
        record.total_deaths = form.total_deaths.data
        record.total_patients = form.total_patients.data
        db.session.commit()
        flash('You have successfully edited the record.')

        # redirect to the departments page
        return redirect(url_for('admin.list_records'))

    form.total_patients.data = record.total_patients
    form.total_deaths.data = record.total_deaths
    form.disease_code.data = record.disease_code
    form.cname.data = record.cname
    form.email.data = record.email

    return render_template('admin/records/record.html', action="Edit",
                           add_record=add_record, form=form,
                           record=record, title="Edit Record")

@admin.route('/records/delete/<string:email>/<string:cname>/<string:disease_code>', methods=['GET', 'POST'])
@login_required
def delete_record(email, cname, disease_code):
    check_admin()

    record = Record.query.get_or_404(email, cname, disease_code)
    db.session.delete(record)
    db.session.commit()
    flash('You have successfully deleted the record.')

    
    return redirect(url_for('admin.list_records'))

    return render_template(title="Delete Record")











