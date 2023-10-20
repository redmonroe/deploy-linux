from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('big_b.html', title='Big Bons!')


# @app.route('/marketing')
# def marketing():
#     return render_template('new_index.html')


@app.get('/home')
def home():
    return "fdl homepage!"
