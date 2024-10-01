# condicional si
# ingresar 5 usuarios
# debe ingresar su nombre y el color de su equipo y alianza
# 3 opciones: ROJO, AZUL Y AMARILLO
# contar cuantos rojos hay 

print("Bienvenido al ANIVERSAIO")
print("")

#inicializacion del contador de los rojo
cont_rojo = 0
cont_amarillo = 0
cont_azul = 0

# ingrese de datos
# USUARIO 1
user1 = input("ingrese nombre del usuario ")

print ("selecione el color de su alianza preferida")
print ("1 si es rojo ")
print ("2 si es amarillo ")
print ("2 si es azul ")

color1 = input("ingrese color de su alianza ")


#if es como si entonces
if color1 =="rojo":
    cont_rojo = cont_rojo + 1

if color1 =="amarillo":
    cont_amarillo = cont_amarillo + 1

if color1 =="azul":
    cont_azul = cont_azul + 1




#usuario 2
user2 = input("ingrese nombre del usuario ")
color2 = input("ingrese color de su alianza ")
if color2 =="rojo":
    cont_rojo = cont_rojo + 1

if color2 =="amarillo":
    cont_amarillo = cont_amarillo + 1

if color2 =="azul":
    cont_azul = cont_azul + 1




#usuario 3
user3 = input("ingrese nombre del usuario ")
color3 = input("ingrese color de su alianza ")
if color3 =="rojo":
    cont_rojo = cont_rojo + 1
else:
 if color3 =="amarillo":
    cont_amarillo = cont_amarillo + 1

if color3 =="azul":
    cont_azul = cont_azul + 1




#usuario 4
user4 = input("ingrese nombre del usuario ")
color4  = input("ingrese color de su alianza ")
if color4 =="rojo":
    cont_rojo = cont_rojo + 1
else:
 if color4 =="amarillo":
    cont_amarillo = cont_amarillo + 1

if color4 =="azul":
    cont_azul = cont_azul + 1



#usuario 5
user5 = input("ingrese nombre del usuario ")
color5 = input("ingrese color de su alianza ")
if color5 =="rojo":
    cont_rojo = cont_rojo + 1
else:
 if color5 =="amarillo":
    cont_amarillo = cont_amarillo + 1
    
    cont_azul = cont_azul + 1
if color5 =="azul":
    cont_azul = cont_azul + 1



print("la cantidad de rojo es: a", cont_rojo)
print("la cantidad de amarillo es: a", cont_amarillo)
print("la cantidad de azul es: a", cont_azul)
