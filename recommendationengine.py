import random
import sqlite3

def globalrecommendations():
    globalrecommendationslist=list()
    handle= open("static/recommendation_files/global.txt")
    rankingdict=dict()
    for line in handle:
        terms=line.strip()
        rankingdict[terms]= rankingdict.get(terms,0)+1
    sorted_ranking = sorted(rankingdict.items(), key=lambda x: x[1], reverse=True)
    
    for x in range(9):
        globalrecommendationslist.append(sorted_ranking[x])
    return globalrecommendationslist

def userrecommendations(user):
    randomterm=randomuserterm(user)
    genre=checkgenre(randomterm)
    userrecommendationslist=findreccomendations(genre)
    return userrecommendationslist

def randomuserterm(user):
    path="static/recommendation_files/" + user +".txt"
    handle= open(path)
    listofterms=list()
    for line in handle:
        terms=line.strip()
        listofterms.append(terms)
    termscount=len(listofterms)
    randomnum=random.randint(0,termscount)
    randomterm=listofterms[randomnum]
    return randomterm

def checkgenre(show):
    con = sqlite3.connect('static/catalog.db')
    cur = con.cursor()
    cur.execute("Select * from showbox where show = ? ",(show,))
    rows = cur.fetchall()
    print(show)
    print(rows)
    genre=None
    for unit in rows:
        genre=unit[1]
    return genre

def findreccomendations(genre):
    reccomendlist=list()
    con = sqlite3.connect('static/catalog.db')
    cur = con.cursor()
    cur.execute("Select * from showbox where genre = ? ",(genre,))
    rows = cur.fetchall()
    for unit in rows:
        reccomendlist.append(unit[0])
    return reccomendlist