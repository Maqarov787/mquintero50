# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
import csv
import random

################################# Code from Dancing Elmos!

def fileParser(file): #reads csv
    with open(file, newline='') as csvfile:
        csvFile = csv.reader(csvfile, delimiter='\n')
        data = []
        for line in csvFile:
            data.append(line)
    return data

def splitHeaders(dataSet): #converts data to dictionary
    dictValues = {}
    for data in dataSet:
        for string in data:
            for count, letter in enumerate(string[:len(string)-1]):
                if letter == ',' and string[count+1].isnumeric():
                    dictValues[string[:count]] = float(string[count+1:])
    return dictValues

def randomizeJob(dict): #randomizes job, weighted
    randVal = random.uniform(0,99.8)
    for data in dict:
        randVal -= dict[data]
        if(randVal <= 0):
            return data

###################################################

app = Flask(__name__)           #create instance of class Flask

CSV_FILE_PATH = 'occupations.csv'

@app.route("/")                 #assign fxn to route

def hello_world():
    #print("the __name__ of this module is... ")
    #print(__name__)
    jobData = fileParser(CSV_FILE_PATH)
    headers = jobData[0][0].split(',')
    numJobData = jobData[1:len(jobData)-1]
    dictValues = splitHeaders(numJobData)
    randJob = randomizeJob(dictValues)
    jobList = "<table><tr><th>Job List</th></tr>"
    for job in dictValues.keys():
        jobList += "<tr><td>" + job + "</td></tr>"
    return "<head><style>table, th, td {border: 1px solid black;}</style></head><body><h1>Trojan Horses: Ethan Sie, Ankita Saha, Marco Quintero, Colyi Chen</h1>Randomly Chosen Job: " + randJob + "<br><br>" + jobList + "</table>"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change; We found this to be true and also that the debugger will print to the terminal that the code has been changed
    app.run()