from flask import Flask, render_template, url_for, request
from time import sleep

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weak-secured")
def weak():
    agent = request.headers.get('User-Agent')   
    if "python-requests" not in agent:
        return render_template("secured.html", ban=False)
    else:
        return render_template("secured.html", ban=True)

if __name__ == "__main__":
    print("Server active...")
    app.run()