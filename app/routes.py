from app import app

@app.route('/')
@app.route('/index')
def index():
    return "flask-deploy-linux!"

@app.get('/home')
def home():
    return "fdl homepage!"