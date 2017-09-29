from project import db

class BaseModel():

	def __init__(*a):
		if len(a) > 1:
			for i in range(1, len(a)):
				self.i = i

	def serialize(self):
		r = {}
		for i in self.a:
			r[i] = getattr(self,i)
		return r	

class Parks(BaseModel, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	lands = db.relationship('Lands', backref='parks')
	attractions = db.relationship('Attractions', backref='parks')
	a = ['id', 'name']

class Lands(BaseModel, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	park_id = db.Column(db.Integer, db.ForeignKey('parks.id'))
	name = db.Column(db.Text, nullable=False)
	attractions = db.relationship('Attractions', backref='lands')
	a = ['id', 'park_id', 'name']

class Attractions(BaseModel, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	park_id = db.Column(db.Integer, db.ForeignKey('parks.id'))
	land_id = db.Column(db.Integer, db.ForeignKey('lands.id'))
	name = db.Column(db.Text, nullable=False)
	a = ['id', 'park_id', 'land_id', 'name']			