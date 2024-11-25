# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Set your API key here
API_KEY = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
        response = requests.get(complete_url)
        data = response.json()

        if data['cod'] == 200:
            main_data = data['main']
            weather_data = data['weather'][0]
            temperature = main_data['temp']
            humidity = main_data['humidity']
            description = weather_data['description']
            return render_template('index.html', city=city, temperature=temperature, humidity=humidity, description=description)
        else:
            error_message = "City not found!"
            return render_template('index.html', error_message=error_message)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
