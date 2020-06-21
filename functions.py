import hashlib
import sqlite3

def check_password(hashed_password, user_password):
    return hashed_password == hashlib.md5(user_password.encode()).hexdigest() 

def validate(username, password):
    con = sqlite3.connect('static/user.db')
    completion = False
    with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    dbPass = row[1]
                    if dbUser==username:
                        completion=check_password(dbPass, password)
    return completion

def writeout(wordlist,user):
    file = open("static/recommendation_files/global.txt","a+") 
    file.write(wordlist+"\n")
    file.close()
    path="static/recommendation_files/" + user +".txt"
    file= open(path,"a+")
    file.write(wordlist+"\n")
    file.close()
def writetime(time):
    file = open("static/recommendation_files/timings.txt","a+") 
    file.write(time+"\n")
    file.close()