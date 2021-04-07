from celery import Celery
from bs4 import BeautifulSoup
import requests
import json

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='db+sqlite:///celery.db')

@app.task
def extract(url):
    result = ''
    try:
        page = requests.get(url, verify=False, timeout=2)
        soup = BeautifulSoup(page.text, 'html.parser')
        result = { 'site': url, 'title': soup.title.string }
    except Exception as e:
        result = { 'site': url, 'error': str(e) }

    return json.dumps(result)
