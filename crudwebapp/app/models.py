from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager



class DiseaseType(UserMixin, db.Model):
	__tablename__ = 'diseasetype'
	id = db.Column(db.Integer, primary_key = True)
	description = db.Column(db.String(140))

	def __repr__(self):
		return '<Disease Type: {}>'.format(self.id)
	

class Country(db.Model):
	__tablename__ = 'country'
	cname = db.Column(db.String(50), primary_key = True)
	population = db.Column(db.BigInteger)

	def __repr__(self):
		return '<Country: {}>'.format(self.cname)

class Disease(db.Model):
	__tablename__ = 'disease'
	disease_code = db.Column(db.String(50), primary_key = True)
	pathogen = db.Column(db.String(20))
	description = db.Column(db.String(140))
	id = db.Column(db.Integer, db.ForeignKey('diseasetype.id'))

	def __repr__(self):
		return '<Disease: {}>'.format(self.disease_code)


class Discover(db.Model):
	__tablename__ = 'discover'
	cname = db.Column(db.String(50), db.ForeignKey('country.cname'), primary_key = True)
	disease_code = db.Column(db.String(50), db.ForeignKey('disease.disease_code'), primary_key = True)
	first_enc_date = db.Column(db.Date)
	
	def __repr__(self):
		return '<Discover: {} {}>'.format(self.cname, self.disease_code)
		
class Users(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(60), unique = True)
	name = db.Column(db.String(30))
	surname = db.Column(db.String(40))
	salary = db.Column(db.Integer, default = 0)
	phone = db.Column(db.String(20))
	cname = db.Column(db.String(50), db.ForeignKey('country.cname'))
	password_hash = db.Column(db.String(128))
	is_admin = db.Column(db.Boolean, default = False)
	
	@property
	def password(self):
		raise AttributeError('password is not readable attribute.')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User: {}>'.format(self.email)


@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))


class PublicServant(db.Model):
	__tablename__ = 'publicservant'
	email = db.Column(db.String(60), db.ForeignKey('users.email'), primary_key = True)
	department = db.Column(db.String(50))
	
	def __repr__(self):
		return '<Public Servant: {}>'.format(self.email)

class Doctor(db.Model):
	__tablename__ = 'doctor'
	email = db.Column(db.String(60), db.ForeignKey('users.email'), primary_key = True)
	degree = db.Column(db.String(20))
	
	def __repr__(self):
		return '<Doctor: {}>'.format(self.email)

class Specialize(db.Model):
	__tablename__ = 'specialize'
	id = db.Column(db.Integer, db.ForeignKey('diseasetype.id'), primary_key = True)
	email = db.Column(db.String(60), db.ForeignKey('doctor.email'), primary_key = True)

	def __repr__(self):
		return '<Specialize: {} {}>'.format(self.id, self.email)

class Record(db.Model):
	__tablename__ = 'record'
	email = db.Column(db.String(60), db.ForeignKey('publicservant.email'), primary_key = True)
	cname = db.Column(db.String(50), db.ForeignKey('country.cname'), primary_key = True)
	disease_code = db.Column(db.String(50), db.ForeignKey('disease.disease_code'), primary_key = True)
	total_deaths = db.Column(db.Integer)
	total_patients = db.Column(db.Integer)

	def __repr__(self):
		return '<Record: {} {} {}>'.format(self.email, self.cname, self.disease_code)
	

