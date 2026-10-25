def calcular_promedios(parcial1, parcial2):
    """Devolverá una lista con el promedio de cada alumno."""
    promedios = []

    for i in range (len(parcial1)):
        promedio = (parcial1[i] + parcial2[i]) / 2 
        promedios = promedios + [promedio]

    return promedios 


def contar_condiciones(promedios):
    """Cuenta cuántos alumnos promocionan, aprueban y desaprueban."""
    promocionan = 0
    aprueban = 0
    desaprueban = 0

    for i in range(len(promedios)):
        if promedios[i] >= 6:
            promocionan = promocionan + 1
        elif promedios[i] >= 4:
            aprueban = aprueban + 1
        else:
            desaprueban = desaprueban + 1

    return promocionan, aprueban, desaprueban



def calcular_promedio_curso(promedios):
    """Devolverá el promedio general del curso."""
    suma = 0 

    for i in range(len(promedios)): 
        suma = suma + promedios[i]

    return suma/ len(promedios)


def mejor_promedio(promedios):
    """Devuelve el mejor promedio del curso."""
    mejor = promedios[0]

    for i in range(len(promedios)):
        if promedios[i] > mejor:
            mejor = promedios[i]

    return mejor


def peor_promedio(promedios):
    """Devuelve el peor promedio del curso."""
    peor = promedios[0]

    for i in range(len(promedios)):
        if promedios[i] < peor:
            peor = promedios[i]

    return peor



