from flask import Flask, request, jsonify

app = Flask(__name__)

def print_data(a):
    print(a)
@app.route('/receiveData', methods=['POST'])
def receive_data():
    data = request.get_json()
    print_data(data)
    print('monir')
    # Process the data here if needed
    return jsonify({"status": "success", "data": data})

# Assurez-vous que cette route est correcte dans votre application Flask
@app.route('/slave.html')
def weather_forecast():
    # Votre logique ici
    pass

@app.route('/master.html')
def master():
    return render_template('master.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=10000)
