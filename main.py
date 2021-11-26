from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def wellcome():
    return "Wellcome....."