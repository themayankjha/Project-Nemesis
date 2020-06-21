from flask import Flask, render_template, redirect, url_for, request, g,json,session
from functions import validate, writeout,writetime
import searchfunc
import reminderengine
import recommendationengine

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
            return redirect(url_for('search'))
    return render_template('login.html', error=error)

@app.route('/search', methods=['GET', 'POST'])
def search():
    messages = session['messages']
    messages=json.loads(messages)
    username=messages['user']
    searches={"searchlength":None}
    if request.method == 'POST':
        searchquery = request.form['search']
        writeout(searchquery,username)
        searches=searchfunc.searchfunc(searchquery)
    return render_template('search.html', username=username, searches=searches)

@app.route('/reminder', methods=['GET', 'POST'])
def reminder():
    messages = session['messages']
    messages=json.loads(messages)
    username=messages['user']
    remstatus=None
    reminders=None
    if request.method == 'POST':
        show = request.form['show']
        setdate = request.form['setdate']
        settime = request.form['settime']
        writeout(show,username)
        writetime(settime)
        remstatus   =  reminderengine.setreminder(show,setdate,settime)
        reminders   =  reminderengine.getreminder(username)
    return render_template('reminder.html', username=username, reminders=reminders , remstatus=remstatus)  

@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    messages = session['messages']
    messages=json.loads(messages)
    username=messages['user']
    globalrecommendations=recommendationengine.globalrecommendations()
    userrecommendations=recommendationengine.userrecommendations(username)
    return render_template('recommendations.html', username=username, globalrecommendations=globalrecommendations , userrecommendations=userrecommendations)

if __name__ == '__main__':
    app.run(debug=True)
