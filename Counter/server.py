from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'count key'

@app.route('/')
def templatename():
    if not 'count' in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)