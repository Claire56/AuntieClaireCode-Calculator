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
@app.route('/', methods=["POST", "GET"])
def homepage():
    if request.method == "POST":
        val1 = int(request.form["num1"])
        val2 = int(request.form["num2"])



        if (request.form.get("add")):
            res = val1 + val2
            return render_template('home.html', val=res)
        if (request.form.get("Sub")):
            res = val1 - val2
            return render_template('home.html', val=res)
        if (request.form.get("div")):
            res = val1 / val2
            return render_template('home.html', val=res)
        if (request.form.get("mult")):
            res = val1 * val2
            return render_template('home.html', val=res)

    else:
        return render_template('home.html', val="na")

    
    


    

#@app.route('calc')
#def calculation():
    #pass

	


if __name__== "__main__":
    app.run(debug = True)
