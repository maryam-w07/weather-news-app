from flask import Flask, request, render_template_string
from weather import weather_and_news
import json

app1 = Flask(__name__)

@app1.route('/', methods=['GET', 'POST'])
def index():
    data = None
    formatted_data = None
    if request.method == 'POST':
        city = request.form['city']
        data = weather_and_news(city)   #data is a dict
        formatted_data = json.dumps(data, indent=4)  # json makes it a string

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Weather App</title>
    </head>
    <body style="font-family: Arial; background-color: #f0f8ff; padding: 20px;">
        <h2> Weather and News App</h2>
        <form method="POST">
            <label>Enter City:</label>
            <input type="text" name="city" required> 
            <input type="submit" value="Get Weather">
        </form>
        {% if formatted_data %}
            <h3>Weather Report</h3>
            <pre style="white-space: pre-wrap; word-wrap: break-word;">{{ formatted_data }}</pre>


            {% if data.temp_map %}
                <h3>Temperature Map</h3>
                <iframe src="{{ data.temp_map }}" width="1000" height="800" style="border:2px solid #ccc; border-radius:10px;"></iframe>
            {% endif %}
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(html, data=data, formatted_data=formatted_data)

if __name__ == "__main__":
    app1.run(debug=True)





