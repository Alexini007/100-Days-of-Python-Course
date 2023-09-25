from flask import Flask, render_template
app = Flask(__name__)
import requests

blog_response = requests.get(url="https://api.npoint.io/3f8df485c36eb1b28c22")
blog_data = blog_response.json()
print(blog_data)

@app.route("/")
def get_all_posts():
    return render_template('index.html', posts=blog_data)

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def individual_post(index):
    for post in blog_data:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)