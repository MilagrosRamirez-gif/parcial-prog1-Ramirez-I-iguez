from validaciones import pedir_cantidad_alumnos
from validaciones import es_nombre_valido
from validaciones import pedir_nota
from procesamiento import calcular_promedio_curso
from procesamiento import calcular_promedios
from procesamiento import mejor_promedio
from procesamiento import peor_promedio
from procesamiento import contar_condiciones


def menu():
    """Muestra las opciones y devuelve lo que Laura elija."""
    opcion = input("""
    NOTA FACIL
1 - Cargar alumnos
2 - Mostrar listado
3 - Mostrar estadisticas
4 - ver ranking 
5 - Buscar alumno
6 - Juegos con nombre
0 - Salir

Elija una opcion: """)

    return opcion


def cargar_alumnos():
    """Carga los datos de los alumnos en listas paralelas."""
    cantidad = pedir_cantidad_alumnos()
    nombres = []
    parcial1 = []
    parcial2 = []

    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre del alumno {i + 1}:")
        while not es_nombre_valido(nombre):
            print("Nombre invalido. Tiene que tener al menos 5 letras y solo espacios")
            nombre = input(f"ingrese el nombre del alumno {i + 1}:")
        nombres = nombres + [nombre]


        nota1 = pedir_nota(1)
        nota2 = pedir_nota(2)
        parcial1 = parcial1 + [nota1]
        parcial2 = parcial2 + [nota2]

    return nombres, parcial1, parcial2


def main():
    """Bucle principal."""
    nombres = []
    parcial1 = []
    parcial2 = []

    opcion = ""
    while opcion != "0":
        opcion = menu()
        match opcion:

            case "1":
                nombres, parcial1, parcial2 = cargar_alumnos()
                print("Alumnos cargados")

            case "2":
                if len(nombres) == 0:
                    print("Aún no hay alumnos cargados")

                else: 
                    for i in range(len(nombres)):
                        print(f"{nombres[i]} - P1: {parcial1[i]} - P2: {parcial2[i]}")

            case "3":
                if len (nombres) == 0:
                    print("Aun no hay alumnos cargados")

                else: 
                    promedios = calcular_promedios(parcial1, parcial2)
                    general = calcular_promedio_curso(promedios)
                    mejor = mejor_promedio(promedios)
                    peor = peor_promedio(promedios)
                    prom, aprueban, desaprueban = contar_condiciones(promedios)

                    posicion_mejor = promedios.index(mejor)
                    posicion_peor = promedios.index(peor)

                    print(f"Promedio general del curso: {general}")
                    print(f"Mejor promedio: {nombres[posicion_mejor]} con {mejor}")
                    print(f"Peor promedio: {nombres[posicion_peor]} con {peor}")
                    print(f"Promocionan: {prom} - Aprueban: {aprueban} - Desaprueban: {desaprueban}")

            case "4":
                print("No hice el ranking perdón profe")

            case "5":
                if len(nombres) == 0:
                    print("Aun no hay alumnos cargados")

                else: 
                    buscado = input("Nombre a buscar:")
                    encontrado = False

                    for i in range(len(nombres)):
                        if nombres[i] == buscado:
                            print(f"{nombres[i]} - P1: {parcial1[i]} - P2: {parcial2[i]}")
                            encontrado = True

                    if not encontrado:
                             print("Ese alumno no esta en la lista")

            case "0":
                print("Hasta luego!")

            case _:
                print("Opcion inexistenta, volver a probar")


main()




                









