from turtle import reset
from helper_functions import adding, modulus,subtraction,multiplication,modulo,power_of
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
def homenew():
    return render_template('homenew.html')

@app.route('/',methods =['POST', 'GET'])
def calculate():
     if request.method == "POST":
        val1 = int(request.form["firstnumber"])
        val2 = int(request.form["secondnumber"])
        operator = request.form["operator"]

        

        if (request.form.get("addNumbers")):
            res = adding(val1, val2)
            return render_template('homenew.html', res)
        if (request.form.get("subtractNumbers")):
            res = subtraction(val1, val2)
            return render_template('homenew.html', res)
        if (request.form.get("multiplyNumbers")):
            res = multiplication(val1, val2)
            return render_template('homenew.html', res)
        if (request.form.get("modulusNumbers")):
            res = modulus(val1, val2)
            return render_template('homenew.html', res)
        if (request.form.get("Numbertopower_of")):
            res = power_of(val1, val2)
            return render_template('homenew.html', res)


        else:

                return render_template('homenew.html', res="notvalid")
 

	



if __name__== "__main__":
    app.run(debug = True)
