from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Chicago'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", posts=posts)


if __name__=="__main__":
    app.run(debug=True)