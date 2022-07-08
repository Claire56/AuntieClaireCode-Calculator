from helper_functions import adding,subtraction,multiplication,modulo,power_of
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
def home():
    return render_template('homenew.html')

@app.route('/DoreenSimpleCalc',methods =['POST', 'GET'])
def DoreenSimpleCalc():
     if request.method == "POST":
        val1 = int(request.form["num1"])
        val2 = int(request.form["num2"])
        operator = request.form["operator"]

        

        if "operator" == "add":
            res = adding(val1, val2)
            return render_template('homenew.html', val=res)
        if "operator" == "subtract":
            res = subtraction(val1, val2)
            return render_template('homenew.html', val=res)
        if "operator" == "multiply":
            res = multiplication(val1, val2)
            return render_template('homenew.html', val=res)
        if "operator" == "modula":
            res = modulo(val1, val2)
            return render_template('homenew.html', val=res)
        if "operator" == "power_of":
            res = power_of(val1, val2)
            return render_template('homenew.html', val=res)


        else:

                return render_template('homenew.html', val="na")
 

	



if __name__== "__main__":
    app.run(debug = True)
