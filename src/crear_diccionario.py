def diccionario_puntos (round):
    dic = {}
    for player in round.keys():
        dic[player] = 0
    return dic

def diccionario_ranking (round, ranking_final):
    for player in round.keys():
        if player not in ranking_final:
            ranking_final[player] = {"kills": 0, "deaths": 0, "assists": 0, "puntos": 0, "mvps": 0}
    return ranking_final
