from fastapi import FastAPI
from routers import employees

app = FastAPI()
app.include_router(employees.router)

@app.get("/")
def home():
    return {"message": "Welcome to Hutech API"}
