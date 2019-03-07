from flask import Flask,render_template, redirect, url_for,request, jsonify, abort,request
from flask_sqlalchemy import SQLAlchemy
from src.flaskbasic import *
from src.flaskbasic.form import StudentForm
import sys
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
_logger_adding = logging.getLogger('Adding results')
_logger_getting = logging.getLogger('Get results')
_logger_update = logging.getLogger('Update results')
_logger_delete = logging.getLogger('Delete results')

class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable= False)
  physics = db.Column(db.Integer)
  maths = db.Column(db.Integer)
  chemistry = db.Column(db.Integer)

@application.route('/', methods=['GET','POST'])
def add_results():
    form = StudentForm()
    _logger_adding.warning("Inside Add Results function")
    _logger_adding.warning("Student form waiting for Input")
    if form.validate_on_submit():
      _logger_adding.warning("When form is submitted with data")
      student = Student(name=form.name.data, physics=form.physics.data, maths=form.maths.data,chemistry=form.chemistry.data,)
      _logger_adding.warning("Student: {} , physics: {} , maths: {}, chemistry: {}".format(form.name.data,form.physics.data,form.maths.data,form.chemistry.data))
      db.session.add(student)
      _logger_adding.warning('student results was added to database')
      db.session.commit()
      _logger_adding.warning("database commit")
      return redirect(url_for("add_results"))
    else:
      return render_template('home.html', form=form)

@application.route('/results', methods=['GET','POST'])
def get_results():
  _logger_getting.warning('retrieving all student results')
  data = Student.query.all()
  _logger_getting.warning('the students results have been collected for {}'.format(data))
  return render_template('results.html', data = data)

@application.route('/results/<int:indexId>', methods=['PUT'])
def update_results(indexId):
  _logger_update.warning("Inside Update function")
  student = Student.query.filter_by(id = indexId).first()

  if not student:
    _logger_update.warning("No Students in database")
    return render_template('home.html',form=form)

  student.name = request.json['name']
  student.physics = request.json.get('physics', "")
  student.maths = request.json.get('maths', "")
  student.chemistry = request.json.get('chemistry', "")
  _logger_update.warning("The updated results are Student Name: {}, Physics: {}, Maths: {}, Chemistry: {}".format(student.name,student.physics,student.maths,student.chemistry)) 
  db.session.commit()
  
  return jsonify({'student':'Pass'})

@application.route('/results/<int:indexId>', methods=['DELETE'])
def delete_student(indexId):
  _logger_delete.warning("Inside Delete function")
  student = Student.query.filter_by(id = indexId).first()

  if not student:
    _logger_delete.warning("No Students in database")
    return jsonify({'message':'No user found'})

  db.session.delete(student)
  _logger_delete.warning("Deleted Student {} and commit to database".format(student))
  db.session.commit()

  return jsonify({'message':'Student found and Deleted'})


