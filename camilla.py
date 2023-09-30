from flask import Flask
import os
from flask_cors import CORS
import csv
import json

# Create the name of the file to get the actual data
basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'static/Melbourne_Temperature.csv')

app = Flask(__name__)

# This line allow me to test my API from a local and public enviroments
CORS(app)
    
@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/search" , methods=['GET'])
def search():
    # Read the CSV file with the correct encodign to avid any unwanted characters
    with open(data_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        headers = next(reader) # Read the header row
        data = []
        for row in reader:
            record = {}
            for i, value in enumerate(row):
                record[headers[i].replace(" ", "")] = value
            data.append(record)
        y = json.dumps(data)
        return y

if __name__ == "__main__":
    # Expose the specific port that are are going to consume with the web page
    port = int(os.environ.get('PORT', 8282))
    app.run(debug=True, host='0.0.0.0', port=port)