from flask import Flask, render_template
import random
import requests
import datetime

app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(blog_url)
blog_data = blog_response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=blog_data)

@app.route('/post/<int:index>')
def post(index):
    print(blog_data)
    return render_template("post.html", posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
