from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def templatename():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def submit():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['fave_language'] = request.form['fave_language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def resultpage():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug = True)