# Prueba Heurística, A* 
import numpy as np

def distancia_heuristica(posicion, objetivo):
    # Calcula la distancia heurística entre la posición y el objetivo
    return abs(posicion - objetivo)

# Genera un vector con valores del 1 al 15
posiciones = np.arange(1, 15)

# Obtiene la posición inicial desde el usuario
posicion_inicial = int(input("Ingresa la posición inicial entre 1 y 12: "))

# Obtiene la posición objetivo
posicion_objetiva = 7

if posicion_inicial < 1 or posicion_inicial > 12:
    print("La posición inicial está fuera del rango válido.")
else:
    # Realiza la búsqueda heurística desde la posición inicial hasta la posición objetivo
    posicion_actual = posicion_inicial
    costo_total = 0
    while posicion_actual != posicion_objetiva:
        # Calcula la distancia heurística para cada posición adyacente a la posición actual
        adyacentes = [posicion_actual - 1, posicion_actual + 1]
        distancias_heuristicas = [distancia_heuristica(posiciones[pos-1], posicion_objetiva) for pos in adyacentes]
        costos = [abs(posiciones[pos-1] - posiciones[posicion_actual-1]) for pos in adyacentes]

        # Selecciona la posición con la menor distancia heurística como siguiente posición
        min_index = np.argmin(distancias_heuristicas)
        siguiente_posicion = adyacentes[min_index]
        costo_siguiente = costos[min_index]

        # Imprime el movimiento realizado y el costo acumulado
        print(f"Moverse desde la posición {posicion_actual} a la posición {siguiente_posicion}")

        # Actualiza la posición actual y el costo total
        posicion_actual = siguiente_posicion
        costo_total += costo_siguiente

    print(f"Se alcanzó la posición objetivo '{posicion_objetiva}'. Costo total: {costo_total}")

