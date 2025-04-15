import numpy as np
import time
import matplotlib.pyplot as plt
import random

def calcular_fuerzas_coulomb(posiciones, cargas):
    n = len(posiciones)
    fuerzas = np.zeros(n)
    
    calcular_fuerzas_dc(posiciones, cargas, 0, n-1, fuerzas)
    
    return fuerzas

def calcular_fuerzas_dc(posiciones, cargas, inicio, fin, fuerzas):
    # Caso base: 0 o 1 partícula
    if fin <= inicio:
        return
    
    # Caso de dos partículas: calcular directamente
    if fin - inicio == 1:
        i, j = inicio, fin
        distancia = posiciones[j] - posiciones[i]
        fuerza = (cargas[i] * cargas[j]) / (distancia * distancia)
        fuerzas[i] += fuerza
        fuerzas[j] -= fuerza
        return
    
    # Dividir
    mitad = (inicio + fin) // 2
    
    # Conquistar: resolver los subproblemas
    calcular_fuerzas_dc(posiciones, cargas, inicio, mitad, fuerzas)
    calcular_fuerzas_dc(posiciones, cargas, mitad+1, fin, fuerzas)
    
    # Combinar: calcular interacciones entre partículas de diferentes mitades
    combinar_fuerzas(posiciones, cargas, inicio, mitad, mitad+1, fin, fuerzas)

def combinar_fuerzas(posiciones, cargas, inicio_izq, fin_izq, inicio_der, fin_der, fuerzas):
   
    for i in range(inicio_izq, fin_izq + 1):
        for j in range(inicio_der, fin_der + 1):
            distancia = posiciones[j] - posiciones[i]
            fuerza = (cargas[i] * cargas[j]) / (distancia * distancia)
            fuerzas[i] += fuerza
            fuerzas[j] -= fuerza

def generar_datos(n, semilla=42):
   
    random.seed(semilla)
    np.random.seed(semilla)
    
    posiciones = np.arange(1, n+1)  
    cargas = np.random.uniform(-5, 5, n)  
    
    return posiciones, cargas

def medir_tiempo(n_valores):
  
    tiempos = []
    resultados = {}
    
    for n in n_valores:
        posiciones, cargas = generar_datos(n)
        
        datos = {
            'posiciones': posiciones.tolist(),
            'cargas': cargas.tolist(),
        }
        
        tiempos_iteracion = []
        for _ in range(5):  # Repetir 5 veces para obtener un promedio
            inicio = time.time()
            fuerzas = calcular_fuerzas_coulomb(posiciones, cargas)
            fin = time.time()
            tiempos_iteracion.append(fin - inicio)
        
        tiempo_medio = np.mean(tiempos_iteracion)
        tiempos.append(tiempo_medio)
        
        resultados[n] = {
            'datos': datos,
            'fuerzas': fuerzas.tolist(),
            'tiempo_medio': tiempo_medio
        }
    
    return tiempos, resultados

def graficar_resultados(n_valores, tiempos):
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_valores, tiempos, 'o-', label='Tiempo medido')
    
    # Ajustar curva de complejidad O(n²)
    coef = np.polyfit(n_valores, tiempos, 2)
    x_fit = np.linspace(min(n_valores), max(n_valores), 100)
    y_fit = coef[0] * x_fit**2 + coef[1] * x_fit + coef[2]
    plt.plot(x_fit, y_fit, '--', label=f'Ajuste O(n²): {coef[0]:.2e}n² + {coef[1]:.2e}n + {coef[2]:.2e}')
    
    plt.xlabel('Número de partículas (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Análisis de Tiempo de Ejecución - Algoritmo D&C para Fuerzas de Coulomb')
    plt.legend()
    plt.grid(True)
    plt.savefig('resultados_tiempos.png')
    plt.show()

def guardar_resultados(resultados, archivo='resultados.txt'):
   
    with open(archivo, 'w') as f:
        for n, datos in resultados.items():
            f.write(f"Tamaño n = {n}\n")
            f.write(f"Tiempo de ejecución: {datos['tiempo_medio']:.6f} segundos\n")
            f.write("Primeras 5 fuerzas: " + str(datos['fuerzas'][:5]) + "\n")
            f.write("-" * 50 + "\n")

if __name__ == "__main__":

    n_valores = [10, 20, 50, 100, 200, 500, 1000]
    
    tiempos, resultados = medir_tiempo(n_valores)
    
    guardar_resultados(resultados)
    
    graficar_resultados(n_valores, tiempos)
    
   