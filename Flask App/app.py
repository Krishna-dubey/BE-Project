from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route('/')
def landing():
    return render_template("login.html")

app.run(debug=True)