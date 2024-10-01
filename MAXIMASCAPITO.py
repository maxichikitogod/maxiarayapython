# Realizar un programa que de solucion a lo sigt: 
# Ingresar 5 alumons (nombre,apellido, y 3 notas)
# Calcular el promedio del alumno
# Calcular el promedio total del curso
# (Compuesto por estos 5 alumnos)
# Calcular la mejor nota por alumno
# Calcular el mejor promedio

def promedio_curso(n1,n2,n3,n4,n5):
    #variable locales
    prom = 0
    prom = (n1,n2,n3,n4,n5)/5
    return prom

def promedio_notas(a, b, c):
    # Ponderaciones
    p1 = 0.2
    p2 = 0.3
    p3 = 0.5
    return (a * p1 + b * p2 + c * p3)

    # nota 1 vale 20%
    # nota 2 vale 30%
    # nota 3 vale 50%

#inicializacion de arreglos
notas = [0,0,0]
alumnos = [0,0,0,0,0]


# Ponderados, que en este caso son CONSTANTES
p = [20,30,50]
prom = [0,0,0,0,0]
print ("bienvenido insuco")
print("")

for i in range (0,5,1):
    print(f"ALUMNO {i+1}")
    #ingrese el nombre del alumno
    alumnos[i] = (input(f"ingrese nombre del alumno: {i+1}"))
    #notas variables ingresadas por teclado
    notas[0]= float(input("Ingrese primera nota " ))
    notas[1] = float(input("Ingrese segunda nota " ))
    notas[2]= float(input("Ingrese tercera nota " ))

    # definicion de las notas
    notas = []
    for i in range(3):
        nota = float(input(f"ingrese la nota {i + 1}: "))
    

    # llamada a la funcion
    prom[1]= promedio_notas(notas[0],notas[1],notas[2])
    print(f"El promedio del alumno {alumnos[i]} es {prom}")
    print("")   


# llamada a la funcion
prom_total = promedio_curso(prom[0],prom[1],prom[2],prom[3],prom[4])
print(f"El promedio del curso 3A es {prom_total}")
print("") 