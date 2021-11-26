from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    return{'data': 'Blog List'}

@app.get('/blog/{id}')
def show(id):
    return{'blog id':id}


@app.get('/blog/{id}/comments')
def show(id):
    return{'blog id with comments':{'1','2'}}