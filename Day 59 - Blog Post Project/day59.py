from flask import Flask, render_template, request
app = Flask(__name__)
import requests
import smtplib

email = "***"
password = "***"

blog_response = requests.get(url="https://api.npoint.io/3f8df485c36eb1b28c22")
blog_data = blog_response.json()
print(blog_data)

@app.route("/")
def get_all_posts():
    return render_template('index.html', posts=blog_data)

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    message_sent = False
    if request.method == 'POST':
        data = request.form
        print(data)
        send_email(data["name"], data["email"], data["phone"], data["message"])
        message_sent = True
        return render_template('contact.html', msg_sent=message_sent)
    return render_template('contact.html', msg_sent=message_sent)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(email, email, email_message)


@app.route('/post/<int:index>')
def individual_post(index):
    for post in blog_data:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)