from models.student_model import Student

students = []
id = 0

def create_student(student):
    global id
    id += 1
    student.id = id
    students.append(student)
    return {'isSuccess':True,'message':'Student Created Successfully','student':student}

def get_students():
    return {'isSuccess':True,'students':students}

def get_student_by_id(studentid):
    for student in students:
        if student.id == studentid:
            return {'isSuccess':True,'student':student}
    return {'isSuccess':False,'message':'Student Not Found'}

def update_student(studentid, updatedStudent):
    for index, student in enumerate(students):
        if student.id == studentid:
            updatedStudent.id = studentid
            students[index] = updatedStudent
            return {'isSuccess':True,'message':'Student Updated Successfully','student':updatedStudent}
    return {'isSuccess':False,'message':'Student Not Found'}

def delete_student(studentid):
    for student in students:
        if student.id == studentid:
            students.remove(student)
            return True
    return False
