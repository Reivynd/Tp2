def dar_estructura(names,goal,goals_avoided,assists):
    players_stats= {}
    for nombre,goles,goles_evitados,asistencias in zip(names,goal,goals_avoided,assists):
      players_stats[nombre] = (goles, goles_evitados, asistencias)
    return  players_stats

def goleador(player_stats):
    nombre_goleador, max_goles = max(player_stats.items(), key=lambda x: x[1][0])
    return nombre_goleador,max_goles[0]

def promedio_ponderado(players_stats):
    max_promedio = float('-inf') 
    mas_influyente = None
    for clave, (goles, goles_evitados, asistencias) in players_stats.items():
        promedio = (goles * 1.5) + (goles_evitados * 1.25) + asistencias
        
        if promedio > max_promedio:
            max_promedio = promedio
            mas_influyente = clave
    
    print(f"El jugador más influyente es: {mas_influyente}")

def promedio_golequipo(players_stats):
    total_goles= sum([stats[0] for stats in players_stats.values()])
    print(f"el promedio de goles del equipo es {total_goles/25}") 


def promedio_goleador(players_stats):
    nombre_goleador, max_goles = goleador(players_stats)
    if max_goles != 0:  
        print(f"El promedio de goles del jugador {nombre_goleador} es de {max_goles / 25} goles por partido")
    else:
        print(f"El goleador del equipo no tiene goles")
       

    
  