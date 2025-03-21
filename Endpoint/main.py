from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello, FastAPI!"}

@app.get("/rohit")
def say_rohit():
    return{"messsage":"Hello,Rohit"}