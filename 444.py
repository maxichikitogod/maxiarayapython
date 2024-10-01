def validar_edad():
    edad = 0 # inicialmente fuera del rango deseado
    while ((edad < 10) or (edad > 20)):
        edad = int(input/"ingrese edad del alumno: ")
        if edad < 10:
            print("la edad no es positiva.. intentalo de nuevo")
        if edad > 20:
            print("la edad muy  grande. debe ser menos o igual a 20")
    return edad

def validar_nota():
    nota = 0 #inicialmente fuera del rango deseado
    while ((nota < 1) or (nota > 7)):
        bota = float(input("ingrese nota del alumno: "))
        if nota < 1:
            print("nota muy pequeño,debe ser mayor o igual que 1")
        if nota > 7:
            print("nota muy grande, debe ser menor o igual a 7.0")
    return nota


def validar_genero():
    genero_validos = ["Masculino" , "femenino", "no binario"]

    while true:
        genero = input("introduce tu genero (masculino, femenino, no binario):")strip() lower()

        if genero in genero_validos:
            print(f"genero{genero}"validado correctamente")
            return genero
        else:
          print("opcion no valida por favor intentar de nuevo")

def promedio (a,b,c):
    prom = (a + b + c)/3
    return prom


print ("bienvenido a septiembre ")      
print ("")

# ALUMNO 1
print("DATOS ALUMNO 1")     
nombre1 = input("ingrese nombre del alumno")
edad1 = validar_edad()
nota1 = validar_nota()
mesada1 = int(input("ingrese mesada del alumno"))

#alumno 2
print("DATOS ALUMNO 2")
nombre2 = input("ingrese nombre del alumno")
edad2 = validar_edad()
nota2 = validar_nota()
mesada2 = int(input("ingrese mesada del alumno"))



#alumno 3
print("DATOS ALUMNO 3")
nombre3 = input("ingrese nombre del alumno")
edad3 = validar_edad()
nota3 = validar_nota()
mesada3 = int(input("ingrese mesada del alumno"))

#calculo 
prom_e = promedio(edad1,edad2,edad3)
prom_n = promedio(nota1,nota2,nota3)


#repuesta 
print("el promedio de las edades de los 3 alumnos es: ",prom_e)
print("el promedio de las notas de los 3 alumnos es: ",prom_n)