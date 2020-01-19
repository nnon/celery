import sqlalchemy
from celery import Celery

app = Celery('tasks', result_backend='sqla+sqlite:///results.db', broker='sqla+sqlite:///broker.db')

@app.task
def add(x, y):
    return x + y
