#1)Arreglos o Array
#2)Validaciones
#Rango numerico por ejemplo: Edad, Notas, Sueldo, Etc...)
#Opciones (por ejemplo: Genero, Alianzas)
#Try Except para controlar error
#Ingresar N personajes para un show en la pampilla (N ingresado por teclado)
#Ingresar por personaje lo siguiente
#NOMBRE
#APELLIDO
#APODO
#SUELDO(rango entre $1.800.000 y $17.000.000)
#FECHA(las opciones son:17 de septiembre, 18 sep,19sept y 20 de sept)
#CAALCULAR PROMEDIO Y NOMBRE COMPLETO(FUNCION)
#MOSTRAR EL ARTISTA AL QUE MAS SE PAGA

def validar_sueldo():
    sueldo = 0
    while ((sueldo < 1000000) or (sueldo > 1700000)):
        try:
            sueldo = int(input("ingrese sueldo del artista"))
            if sueldo < 1000000:
                print("sueldo muy bajo, debe ser mayor o igual que 1000000 intentelo de nuevo")
            if sueldo > 17000000:
                print("sueldo muy alto, debe ser menor o mayor que 17000000 intentelo de nuevo")
        except ValueError:
                print("debe escribir el sueldo comom entero")
        print("")
        return sueldo
    
def validar_dia():
     dias_validos = ['17-09', '19-09','20-09']

     while True:
          dia = input("introduce fecha del show (17-09. 18-09, 19.09)")

          if dia in dias_validos:
               print(f"fecha '{dia}' valida correctamente.")
               print("")
               return dia
          else:
               print("opcion no valida. porfavor. intenta de nuevo")
                      
def validar_positivo(numero):
    if numero > 0:
         return True
    else:
         return False
        

print("bienvenido a la pampilla insuco")
print("")

n = int(input("ingrese cantidad de artistas: "))
validar_positivo(n)