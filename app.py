from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")

def first_webpage():
    name = "Hemani"
    return render_template("index.html", student_name = name)

app.run(debug=True)
