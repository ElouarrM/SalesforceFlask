from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = 'weather_data.json'

def read_data_from_file():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def write_data_to_file(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/receiveData', methods=['POST'])
def receive_data():
    data = request.get_json()
    write_data_to_file(data)  # Stocker les données dans le fichier JSON
    return jsonify({"status": "success", "data": data})

@app.route('/master.html')
def master():
    data = read_data_from_file()  # Lire les données du fichier JSON
    return render_template('master.html', data=data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
