from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['post'])
def show_info():
    return render_template('result.html', name = request.form['name'],  dojo = request.form['dojo'], language = request.form['language'], comment = request.form['comment'])


app.run(debug=True)
