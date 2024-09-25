# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "<head>\n<style>\ntable, th, td {\n border: 1px solid black; \n }\n</style>\n</head>\n<body>\n<h1>Trojan Horses</h1>\n<table>\n<tr>\n<th>Job Class</th>\n<th>Percentage</th>\n<tr>\n<td>Management</td>\n<td>6.1</td>\n</tr>\n<tr>\n<td>Business and Financial operations</td>\n<td>5.0</td>\n</tr>\n<tr>\n<td>Computer and Mathematical</td>\n<td>2.7</td>\n</tr>\n<tr>\n<td>Architecture and Engineering</td>\n<td>1.7</td>\n</tr>\n<tr>\n<td>Life, Physical and Social Science</td>\n<td>0.9</td>\n</tr>\n<tr>\n<td>Community and Social Service</td>\n<td>1.6</td>\n</tr>\n<tr>\n<td>Legal</td>\n<td>0.8</td>\n</tr>\n<tr>\n<td>Education, training and library</td>\n<td>6.1</td>\n</tr>\n<tr>\n<td>Arts, design, entertainment, sports and media</td>\n<td>1.7</td>\n</tr>\n<tr>\n<td>Healthcare practioners and technical</td>\n<td>5.5</td>\n</tr>\n<tr>\n<td>Healthcare support</td>\n<td>2.8</td>\n</tr>\n<tr>\n<td>Protective service</td>\n<td>2.3</td>\n</tr>\n<tr>\n<td>Food preparation and serving</td>\n<td>8.3</td>\n</tr>\n<tr>\n<td>Building and grounds cleaning and maintenance</td>\n<td>3.7</td>\n</tr>\n<tr>\n<td>Personal care and service</td>\n<td>4.0</td>\n</tr>\n<tr>\n<td>Sales</td>\n<td>10.2</td>\n</tr>\n<tr>\n<td>Office and administrative support</td>\n<td>15.1</td>\n</tr>\n<tr>\n<td>Farming, fishing and forestry</td>\n<td>0.6</td>\n</tr>\n<tr>\n<td>Construction and extraction</td>\n<td>4.3</td>\n</tr>\n<tr>\n<td>Installation, maintenance and repair</td>\n<td>3.8</td>\n</tr>\n<tr>\n<td>Production</td>\n<td>6.1</td>\n</tr>\n<tr>\n<td>Transportation and material moving</td>\n<td>6.5</td>\n</tr>\n</table>\n</body>"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
