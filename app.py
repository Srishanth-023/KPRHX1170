from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/live')
def live_monitoring():
    return render_template("live.html")

@app.route('/crimerate')
def crimerate():
    return render_template("crimerate.html")

@app.route('/criminalrecords')
def criminalrecords():
    return render_template("criminalrecords.html")

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")



if __name__ == '__main__':
    app.run(debug=True)
