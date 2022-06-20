from helper_functions import adding, subtraction, multiplication, modulo
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
        operator = request.form["operator"]



        if operator == "add":
            res = adding(val1, val2)
            return render_template('home.html', val=res)
        if operator == "subtract":
            res = subtraction(val1, val2)
            return render_template('home.html', val=res)
        if operator == "multiply":
            res = multiplication(val1, val2)
            return render_template('home.html', val=res)
        if operator == "modula":
            res = modulo(val1, val2)
            return render_template('home.html', val=res)

    else:
        return render_template('home.html', val="na")

    
    


    

#@app.route('calc')
#def calculation():
    #pass

	


if __name__== "__main__":
    app.run(debug = True)
