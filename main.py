from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def wellcome():
    return{'data': {'suhail','jahangir','sikander'}}


@app.get("/about")
def wellcome():
    return{'about Page': {'this is about page '}}