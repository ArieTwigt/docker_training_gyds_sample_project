from flask import Flask
import os

city = os.environ.get("CITY")
city = "World" if city is None else city

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, {city}!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")