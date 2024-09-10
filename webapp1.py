from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Initialize weather data storage
weather_data = []

# Function to update the weather data
def update_weather_data(new_data):
    global weather_data
    weather_data=new_data

@app.route('/receiveData', methods=['POST'])
def receive_data():
    data = request.get_json()
    update_weather_data(data)  # Update the weather data when receiving new data
    return jsonify({"status": "success", "data": data})

# Route to return weather data as JSON
@app.route('/weather_data', methods=['GET'])
def get_weather_data():
    return jsonify(weather_data)

# Serve the HTML page
@app.route('/')
def display_weather_page():
    # HTML template embedded in the Flask route using render_template_string
    template = """
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
        <script>
            function fetchWeatherData() {
                fetch('/weather_data')
                    .then(response => response.json())
                    .then(data => {
                        const tableBody = document.getElementById('forecastTableBody');
                        tableBody.innerHTML = '';  // Clear the table

                        data.forEach(entry => {
                            const row = document.createElement('tr');
                            row.innerHTML = `
                                <td>${entry.time}</td>
                                <td>${entry.temperature}</td>
                                <td>${entry.humidity}</td>
                                <td>${entry.windSpeed}</td>
                            `;
                            tableBody.appendChild(row);
                        });
                    });
            }

            // Automatically refresh the weather data every 5 seconds
            setInterval(fetchWeatherData, 1000);

            // Fetch data when the page loads
            window.onload = fetchWeatherData;
        </script>
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
            <tbody id="forecastTableBody"></tbody>
        </table>
    </body>
    </html>
    """
    return template

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
