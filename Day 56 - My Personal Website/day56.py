from flask import Flask
app = Flask(__name__)
from flask import render_template

@app.route("/")
def hello_home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)