import random
import time

def generar_paradas(cantidad_paradas, max_autonomia=1, semilla = None):

    if semilla is not None:
        random.seed(semilla)
    
    paradas = []
    nueva_parada = 0
    
    for _ in range(cantidad_paradas):
        nueva_parada += random.randint(1, max_autonomia)
        paradas.append(nueva_parada)

    random.shuffle(paradas)
    return paradas

def elegir_paradas(paradas, max_autonomia):

    kilometros_recorridos = 0
    autonomia_km = max_autonomia
    paradas_elegidas = []

    paradas.sort()

    for i in range(len(paradas)):
        

        tramo = paradas[i] - kilometros_recorridos

        if tramo > max_autonomia:
            return [("No es posible completar el recorrido")]
    
        if tramo > autonomia_km:
            paradas_elegidas.append(paradas[i-1]) 
            autonomia_km = max_autonomia
        
        autonomia_km -= tramo
        kilometros_recorridos += tramo
        
    return paradas_elegidas
        

def prog():

    semilla_tp = 42
    max_autonomia = 7

    paradas_5 = generar_paradas(5,max_autonomia,semilla_tp)
    paradas_10 = generar_paradas(10,max_autonomia,semilla_tp)
    paradas_50 = generar_paradas(50,max_autonomia,semilla_tp)
    paradas_100 = generar_paradas(100,max_autonomia,semilla_tp)
    paradas_250 = generar_paradas(250,max_autonomia,semilla_tp)
    paradas_500 = generar_paradas(500,max_autonomia,semilla_tp)
    paradas_1000 = generar_paradas(1000,max_autonomia,semilla_tp)
    paradas_2000 = generar_paradas(2000,max_autonomia,semilla_tp)
    paradas_4000 = generar_paradas(4000,max_autonomia,semilla_tp)
    
    print("Paradas elegidas y tiempos de ejecución","\n")

    tiempo = time.time()
    paradas_elegidas_5 = elegir_paradas(paradas_5, max_autonomia)
    print("5 paradas","\n" ,"Paradas elegidas:",paradas_elegidas_5)
    print("\n" ,time.time() - tiempo," segundos","\n")

    tiempo = time.time()
    paradas_elegidas_10 = elegir_paradas(paradas_10, max_autonomia)
    print("10 paradas","\n" ,"Paradas elegidas:",paradas_elegidas_10)
    print("\n" ,time.time() - tiempo," segundos","\n")

    tiempo = time.time()
    paradas_elegidas_50 = elegir_paradas(paradas_50, max_autonomia)
    print("50 paradas","\n" ,"Paradas elegidas:",paradas_elegidas_50)
    print("\n" ,time.time() - tiempo," segundos","\n")

    tiempo = time.time()
    paradas_elegidas_100 = elegir_paradas(paradas_100, max_autonomia)
    print("100 paradas","\n" ,"Paradas elegidas:",paradas_elegidas_100)
    print("\n" ,time.time() - tiempo," segundos","\n")

    tiempo = time.time()
    paradas_elegidas_250 = elegir_paradas(paradas_250, max_autonomia)
    print("250 paradas","\n" ,"Paradas elegidas:",paradas_elegidas_250)
    print("\n" ,time.time() - tiempo," segundos","\n")

    tiempo = time.time()
    paradas_elegidas_500 = elegir_paradas(paradas_500, max_autonomia)
    print("500 paradas","\n" ,"Paradas elegidas:",paradas_elegidas_500)
    print("\n" ,time.time() - tiempo," segundos","\n")

    tiempo = time.time()
    paradas_elegidas_1000 = elegir_paradas(paradas_1000, max_autonomia)
    print("1000 paradas","\n" ,"Paradas elegidas:",paradas_elegidas_1000)
    print("\n" ,time.time() - tiempo," segundos","\n")

    tiempo = time.time()
    paradas_elegidas_2000 = elegir_paradas(paradas_2000, max_autonomia)
    print("2000 paradas","\n" ,"Paradas elegidas:",paradas_elegidas_2000)
    print("\n" ,time.time() - tiempo," segundos","\n")

    tiempo = time.time()
    paradas_elegidas_4000 = elegir_paradas(paradas_4000, max_autonomia)
    print("4000 paradas","\n" ,"Paradas elegidas:",paradas_elegidas_4000)
    print("\n" ,time.time() - tiempo," segundos","\n")


prog()