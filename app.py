import os
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f'Hello! This page has been visited {count} times.'
