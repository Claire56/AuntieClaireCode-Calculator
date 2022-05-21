from helper_functions import *
# from flask import Flask ,render_template, session,jsonify, request ,redirect, make_response
# from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from flask import Flask ,render_template,request ,redirect, make_response



app = Flask('__name__')
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "nabawanda"


#add your routes here
@app.route('/')
def homepage():

	return render_template('home.html')

@app.route('/calculate')
def calculation():
    pass

	


if __name__== "__main__":
    app.run(debug = True)
