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
    userrecommendationslist=None
    return userrecommendationslist