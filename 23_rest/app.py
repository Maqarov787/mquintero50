'''
Marco Quintero
Run DMD - Danny, Marco
SoftDev
K23 - A RESTful Journey Skyward
2024-11-20
time spent: 0.7
'''


from flask import Flask, render_template
import os
import urllib.request
import json

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)
file = open("key_nasa.txt", "r")
api_key = file.read().strip()

@app.route("/")
def main():
    with urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=" + api_key) as response:
        '''html = response.read() #reads the page's source code
        print(html)
        data = json.loads(html) #converts the page's source code into a python dictionary'''
        data = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
        #print(data)
    return render_template('main.html', url=data["hdurl"], explanation=data["explanation"])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
