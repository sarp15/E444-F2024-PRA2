# from flask import Flask
# app = Flask(__name__)

# @app.route('/') 
# def index():
#     return '<h1>Hello World!</h1>'

# @app.route('/user/<name>') 
# def user(name):
#     return '<h1>Hello, {}!</h1>'.format(name)



from flask import Flask, render_template
from flask_bootstrap import Bootstrap 
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# @app.route('/') 
# def index():
#     return render_template('index.html')

@app.route('/user/<name>') 
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())

from datetime import datetime
@app.route('/') 
def index():
    return render_template('index.html', current_time=datetime.utcnow())

if __name__ == '__main__': 
    app.run(port=5001)
