from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '_main_':
    app.run(debug=False, port = 8000)