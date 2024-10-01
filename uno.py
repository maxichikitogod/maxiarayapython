# realizar un programa que de solucion a los sigt:
# ingresar 5 alumnos (nombre,apellido, y 3 notas)
# calcular el promedio del alumno
# calcular el promedio total del curso
# (compuesto por estos 5 alumnos)
# calcular la mejor nota por alumno
# calcular el mejor promedio

def promedio_curso(n1,n2,n3,n4,n5):
    #variable locales
    prom = 0
    prom = (n1+n2+n3+n4+n5)/5   
    return prom 

def promedio_nota(a,b,c):
    #variable locales
    prom = 0
    prom = (p1*n1*p2*n2*p3*n3)/100
    return prom 

# nota 1 vale 20%
# nota 2 vale 30%
# nota 4 vale 50%

print("hola")
print("")

# ponderados, que en este caso son CONSTANTES
p1 = 20
p2 = 30 
p3 = 50

# notas variable ingresada por teclado
nota1 = float(input("ingrese primera nota"))
nota2 = float(input("ingrese segunda nota"))
nota3 = float(input("ingrese tercera nota"))

prom = promedio_notas(nota1,nota2,nota3,p1,p2,p3)
print(f"elpromedio del alumno es{prom}")