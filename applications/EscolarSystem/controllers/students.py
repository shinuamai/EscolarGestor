# controllers/students.py
from gluon import response

def index():
    return dict()

def register_student():
    # Implementa la lógica para manejar la solicitud de registro de estudiantes
    return response.json({'status': 'success'})