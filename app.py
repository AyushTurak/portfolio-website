from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/services')
def services():
    return render_template('services.html')


app.run(debug=True)


