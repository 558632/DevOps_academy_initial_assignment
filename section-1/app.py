from flask import Flask

app = Flask(__name__)

def home():
    return "This is dockerized flask application."
app.add_url_rule("/", "home", home)

# server will start only if this file is the entrance point of the programm
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)