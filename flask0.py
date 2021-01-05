from flask import Flask
app = Flask(__name__)

@app.route("/status")
def status():
    return "Alive"

@app.route("/login")
def login():
    return "login"

if __name__ == "__main__":
    app.run(debug=True)