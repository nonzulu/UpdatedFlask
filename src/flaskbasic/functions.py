from flask_sqlalchemy import SQLAlchemy
from src.flaskbasic.models import Student
from src.flaskbasic.form import StudentForm
from src.flaskbasic.wsgi import db
# from src.flaskbasic.wsgi import Student
import os

class functions():

      def putData():
            form = StudentForm()
            student = Student(name=form.name.data, physics=form.physics.data, maths=form.maths.data,chemistry=form.chemistry.data,)
            db.session.add(student)
            db.session.commit()

      def readData():
            results = Student.query.all()
            return results

      def readName(learner,student_id):
            studentname = Student.query.filter_by(name=learner, id=student_id).all()
            for student_name in studentname:
                  return student_name.name


      def readResults(student_id,learner,physcalS, mathematics, chem ):
            studentname = Student.query.filter_by(id=student_id, name=learner, physics=physcalS, maths= mathematics, chemistry=chem     ).all()
            for student_name in studentname:
                  return student_name.id,student_name.name,student_name.physics,student_name.maths,student_name.chemistry

      # def updates(student_id):
      #       student_data = Student.query.get_or_404(student_id)
      #       form = StudentForm()
      # if form.validate_on_submit():
      #       student_data.name = form.name.data
      #       student_data.physics = form.physics.data
      #       student_data.maths = form.maths.data
      #       student_data.chemistry = form.chemistry.data
      #       db.session.commit()
            
      def delete(student_id):
            student_results = Student.query.get_or_404(student_id)
            db.session.delete(student_results)
            db.session.commit() 

      def resetResults():
          db.drop_all()
			
	