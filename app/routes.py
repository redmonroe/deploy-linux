from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('coming_soon.html', title='Big Bons!')

@app.route('/marketing')
def marketing():
    return render_template('new_index.html')


@app.get('/home')
def home():
    return "fdl homepage!"
