# Prueba Exhaustiva, búsqueda en anchura
import numpy as np

# Se asume que el motor posee 12 posiciones de las cuales no se podrá salir
print("La posición de la maquina se encuentra en el rango de posiciones 1-12")

# Obtiene la posición inicial "B" del usuario, donde se hará la búsqueda del punto "A"
posicion_inicial = int(input("Ingrese la posición inicial: "))

# Se define un vector de posiciones para el motor y una posición objetiva simulando el valor de "A"
posiciones=np.arange(1, 12)
posicion_objetiva = posiciones[4]

recorrido = []

# Verifica si las posiciones están dentro del rango válido
if posicion_inicial < 1 or posicion_inicial > 12:
    print("La posición inicial está fuera del rango válido.")
else:   
    # Búsqueda del punto "A" en ambos sentidos desde el punto "B"
    if posicion_inicial != posicion_objetiva:

        i = posicion_inicial
        while i >= posicion_objetiva:
            recorrido.append(i)
            i-=1

        i = posicion_inicial    
        while i <= posicion_objetiva:
            recorrido.append(i)
            i+=1

        print(f"El recorrido hasta llegar a la posición correcta ({posicion_objetiva}) es: {recorrido}")

    else:
        print(f"La posición {posicion_inicial} es la correcta")
