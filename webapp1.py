from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Initialize weather data storage
weather_data = []

def update_weather_data(new_data):
    global weather_data
    weather_data.extend(new_data)  # Update the weather data list
 
@app.route('/receiveData', methods=['POST'])
def receive_data():
    data = request.get_json()
    update_weather_data(data)  # Update the weather data when receiving new data
    return jsonify({"status": "success", "data": data})

@app.route('/showWeatherData')
def show_weather_data():
    global weather_data
    # Build an HTML string to display weather data
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weather Data</title>
        <style>
            table {width: 100%; border-collapse: collapse;}
            th, td {border: 1px solid black; padding: 8px; text-align: center;}
            th {background-color: #f2f2f2;}
        </style>
    </head>
    <body>
        <h1>Weather Data</h1>
        <table>
            <thead>
                <tr>
                    <th>Time</th>
                    <th>Temperature (°C)</th>
                    <th>Humidity (%)</th>
                    <th>Wind Speed (m/s)</th>
                </tr>
            </thead>
            <tbody>
    """

    # Add weather data to the table
    for entry in weather_data:
        html_content += f"""
            <tr>
                <td>{entry['time']}</td>
                <td>{entry['temperature']}</td>
                <td>{entry['humidity']}</td>
                <td>{entry['windSpeed']}</td>
            </tr>
        """

    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """
    
    return html_content

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
