from flask import Flask, render_template, redirect, url_for, request, g,json,session
from functions import validate, writeout
import searchfunc
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
            return redirect(url_for('dashboard'))
    return render_template('loginpage.html', error=error)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    messages = session['messages']
    messages=json.loads(messages)
    username=messages['user']
    searches={"searchlength":None ,"showname": None, "genre_chname": None,"images": None, "desc": None, "timings": None, "ch_number": None}
    if request.method == 'POST':
        searchquery = request.form['search']
        writeout(searchquery,username)
        searches=searchfunc.searchfunc(searchquery)
    return render_template('dashboard.html', username=username, searches=searches)

if __name__ == '__main__':
    app.run(debug=True)
