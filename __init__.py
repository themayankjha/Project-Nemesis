from flask import Flask, render_template, redirect, url_for, request, g,json,session
from functions import validate

app = Flask(__name__)
app.secret_key = "DV12WKIXobwUOpN1Xuo5sJxEFQtKMY6O"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            messages = json.dumps({"user":username})
            session['messages'] = messages
            return redirect(url_for('dashboard', messages=messages))
    return render_template('loginpage.html', error=error)

@app.route('/dashboard')
def dashboard():
    messages = request.args['messages']
    messages = session['messages']
    return render_template("dashboard.html", messages=json.loads(messages))

if __name__ == '__main__':
    app.run(debug=True)
