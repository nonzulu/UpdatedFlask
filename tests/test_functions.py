# from flask_sqlalchemy import SQLAlchemy
# from flaskbasic.wsgi import *
from src.flaskbasic.functions import functions
import pytest

fun = functions

def test_student_name():
    assert fun.readName('Lwando',2) == 'Lwando'

def test_all_results():
    assert fun.readResults(2, 'Lwando',10,60,10) == (2, 'Lwando', 10, 60, 10)

    
    
	

		