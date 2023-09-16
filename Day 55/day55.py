from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello World! </h1>' \
           '<p>Paragraph</p>'


@app.route('/bye')
@make_bold
def bye():
    return 'Bye'


@app.route("/username/<name>/<int:number>")
def hello(name, number):
    return f"Hello, {name} , your ID: {number}!"


if __name__ == "__main__":
    app.run(debug=True)

