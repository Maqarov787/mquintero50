'''
Marco Quintero
Ghidorah - Mark, Danny,Marco
SoftDev
K15 - Flask Forms
2024-10-07
time spent: 0.5
'''

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session           #facilitate user session
from flask import redirect          #facilitate user to different route

app = Flask(__name__)    #create Flask object
app.secret_key = 'BAD_SECRET_KEY' #randomly generate one later

@app.route("/")
def disp_loginpage():
    return render_template( 'login.html' , method = request.method)


@app.route("/response", methods=['POST']) # , methods=['GET', 'POST'])
def authenticate():
    session['username'] = request.form['username']
    return render_template('response.html', username=session['username'], method=request.method)
'''@
def logout():'''
    

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
