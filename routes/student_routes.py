from fastapi import APIRouter, Response
from models.student_model import Student
from controllers.student_controller import *

studentRouter = APIRouter()

@studentRouter.post('/students')
def create(student: Student, response: Response):
    response.status_code = 201
    return create_student(student)

@studentRouter.get('/students')
def get_all(response: Response):
    response.status_code = 200
    return get_students()

@studentRouter.get('/students/{studentid}')
def get_by_id(studentid: int, response: Response):
    result = get_student_by_id(studentid)
    if not result['isSuccess']:
        response.status_code = 404
    return result

@studentRouter.put('/students/{studentid}')
def update(studentid: int, student: Student, response: Response):
    result = update_student(studentid, student)
    if not result['isSuccess']:
        response.status_code = 404
    return result

@studentRouter.delete('/students/{studentid}')
def delete(studentid: int, response: Response):
    if delete_student(studentid):
        response.status_code = 204
        return
    response.status_code = 404
    return {'isSuccess':False,'message':'Student Not Found'}
