from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Variable globale pour stocker les données
weather_data = {}

@app.route('/receiveData', methods=['POST'])
def receive_data():
    global weather_data
    data = request.get_json()
    weather_data = data  # Stocker les données dans la variable globale
    return jsonify({"status": "success", "data": data})

@app.route('/master.html')
def master():
    global weather_data
    return render_template('master.html', data=weather_data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
