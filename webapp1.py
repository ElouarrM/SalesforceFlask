from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

def update_weather_data(new_data):
    try:
        # Read existing data from weather_data.json
        with open('static/weather_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # Create a new file if it does not exist
        data = []

    # Write updated data back to static/weather_data.json
    with open('static/weather_data.json', 'w') as file:
        json.dump(new_data, file, indent=4)

@app.route('/receiveData', methods=['POST'])
def receive_data():
    data = request.get_json()
    update_weather_data(data)
    return jsonify({"status": "success", "data": data})

@app.route('/master.html')
def master():
    return render_template('master.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
