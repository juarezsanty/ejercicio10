def procesar_ronda(round, ranking_final):
    point_in_round ={'Shadow': 0, 'Blaze': 0, 'Viper': 0, 'Reaper': 0, 'Frost':0}
    for player_name, player_data in round.items():
        points = procesar_jugador(player_name, player_data, ranking_final)
        point_in_round[player_name] = points
    mvp = max(point_in_round, key=point_in_round.get)
    ranking_final[mvp]["mvps"] += 1
    for player_name, points in point_in_round.items():
        ranking_final[player_name]["puntos"] += points
    return sorted(ranking_final.items(), key=lambda x: x[1]["puntos"], reverse=True)



def procesar_jugador(player_name, player_data, ranking_final):
    kills = player_data["kills"]
    deaths = player_data["deaths"]
    assists = player_data["assists"]
    ranking_final[player_name]["kills"] += kills
    ranking_final[player_name]["deaths"] += deaths
    ranking_final[player_name]["assists"] += assists
    points = kills*3 + assists - deaths
    return points