def MasGrande(Entrada_evaluar):
    # Quitar los espacios en blanco
    Entrada_evaluar = Entrada_evaluar.replace(" ", "")

    # Separar el nombre del artículo y los tamaños en pequeños modulos
    modulos = Entrada_evaluar.split(",")
    
    # Validar el nombre del artículo
    nombre= modulos[0]
    if not nombre.isalpha() or len(nombre) < 2 or len(nombre) > 15:
        return False #, "Nombre de artículo inválido"

    # Validar los tamaños
    tamaños = modulos[1:]
    if len(tamaños) < 1 or len(tamaños) > 5:
        return False #, "Debe haber entre 1 y 5 tamaños"

    temp = 0 #variable temporal para ver si estan en orden ascendente
    for size in tamaños:
        try:
            size = int(size)
            if size < 1 or size > 48:
                return False #, f"Tamaño '{size}' fuera del rango permitido"
            if size <= temp:
                return False #, f"Tamaños deben ser ingresados en orden ascendente"
            temp = size
        except ValueError:
            return False  #, f"Tamaño '{size}' no es un número entero"

    return True , "Entrada Válida"


