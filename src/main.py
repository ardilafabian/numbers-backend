from flask import Flask, request, make_response, redirect
from src.blueprints.blueprint_numbers import numbers

app = Flask(__name__)

app.register_blueprint(numbers, url_prefix="/numbers")

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return f'Hello world, Your IP => {user_ip}'


