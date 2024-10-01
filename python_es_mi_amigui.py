def validar_edad():
    edad = 0  # Inicialmente fuera del rango deseado
    while (edad < 10) or (edad > 20):
        edad = int(input("Ingrese edad del alumno (debe estar entre 10 y 20): "))
        if edad < 10:
            print("La edad no es válida. Debe ser mayor o igual a 10.")
        if edad > 20:
            print("La edad no es válida. Debe ser menor o igual a 20.")
    return edad

def validar_nota():
    nota = 0  # Inicialmente fuera del rango deseado
    while (nota < 1) or (nota > 7):
        nota = float(input("Ingrese nota del alumno (debe estar entre 1 y 7): "))
        if nota < 1:
            print("La nota no es válida. Debe ser mayor o igual a 1.")
        if nota > 7:
            print("La nota no es válida. Debe ser menor o igual a 7.")
    return nota

def validar_especialidad():
    especialidades_validas = ["programación", "administración", "contabilidad"]
    while True:
        especialidad = input("Introduce la especialidad (programación, administración, contabilidad): ").strip().lower()
        if especialidad in especialidades_validas:
            print(f"Especialidad {especialidad} validada correctamente.")
            return especialidad
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def promedio(a, b, c):
    return (a + b + c) / 3

print("Bienvenido a septiembre tikitikitii uyui")
print("")

# Inicializando los arreglos (listas)
nombres = ["", "", ""]
especialidades = ["", "", ""]
notas = [0, 0, 0]
edades = [0, 0, 0]
mesadas = [0, 0, 0]

# Recorriendo el ciclo para ingresar datos de los alumnos
for i in range(3):
    print(f"DATOS ALUMNO {i + 1}")
    nombres[i] = input("Ingrese nombre del alumno: ")
    especialidades[i] = validar_especialidad()
    edades[i] = validar_edad()
    notas[i] = validar_nota()
    mesadas[i] = int(input("Ingrese mesada del alumno: "))

# Cálculos del promedio de edades y notas
prom_e = promedio(edades[0], edades[1], edades[2])
prom_n = promedio(notas[0], notas[1], notas[2])

# Resultado de promedios
print("El promedio de las edades de los 3 alumnos es:", prom_e)
print("El promedio de las notas de los 3 alumnos es:", prom_n)

# Encontrar el promedio más alto y el detalle del alumno correspondiente
indice_max_nota = notas.index(max(notas))
nombre_max_nota = nombres[indice_max_nota]
especialidad_max_nota = especialidades[indice_max_nota]
nota_max_nota = notas[indice_max_nota]

print(f"\nEl alumno con la nota más alta es {nombre_max_nota} con una nota de {nota_max_nota}.")
print(f"La especialidad de este alumno es {especialidad_max_nota}.")
