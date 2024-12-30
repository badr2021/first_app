from flask import Flask,render_template
import jinja2

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("page1.html",pagetitle="Main Page")
@app.route("/about")
def about():
    return render_template("about.html",pagetitle="About")
if __name__== "__main__":

    app.run(debug=True ,port=9000)
