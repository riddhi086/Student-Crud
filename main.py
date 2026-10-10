from fastapi import FastAPI
from routes.student_routes import studentRouter

app = FastAPI()

app.include_router(studentRouter)
