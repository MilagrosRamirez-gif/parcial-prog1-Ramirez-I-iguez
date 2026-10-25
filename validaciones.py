def es_entero_valido(texto, minimo, maximo):
    """Devuelve True si texto es un entero dentro del rango dado."""

    if len(texto) == 0:
        return False

    for caracter in texto:
        if not ("0" <= caracter <= "9"):
            return False 

    numero = int(texto)
    return minimo <= numero <= maximo


def pedir_cantidad_alumnos():
    cantidad = input("Ingrese la cantidad de alumnos (1 a 30)")

    while not es_entero_valido(cantidad, 1, 30):
        print("Valor invalido. Tiene que ser un entero entre 1 y 30")
        cantidad = input("ingrese la cantidad de alumnos (1 a 30):")

    return int(cantidad)


def es_nombre_valido(nombre):
    """Devuelve True si el nombre tiene al menos 5 letras y espacios."""

    if len(nombre) < 5:
        return False 
    
    for caracter in nombre:
        if not (("a" <= caracter <= "z") or
                ("A" <= caracter <= "Z") or
                caracter == " "):
            return False
    return True


def pedir_nota(parcial):
    """Pide la nota de un parcial y la valida entre 0 y 10."""
    nota = input(f"Ingrese la nota del parcial {parcial} (0 a 10): ")

    while not es_entero_valido(nota, 0, 10):
        print("Nota inválida. Debe ser un entero entre 0 y 10.")
        nota = input(f"Ingrese la nota del parcial {parcial} (0 a 10): ")

    return int(nota)



