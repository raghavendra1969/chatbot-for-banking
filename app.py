from flask import Flask, render_template, request
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.form["msg"]
    return get_response(user_msg)

if __name__ == "__main__":
    # Running Flask on port 5050
    app.run(host='127.0.0.1', port=5050, debug=True)
