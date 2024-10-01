# programa de calculo
# ingresar la cantidad de alumno del curso
# para cada alumno debe ingresar
# nombre
# genero
# notas (nota 1, nota 2, nota 3)
# calcular promedio para cada alumno 
# calcular cuantas mujeres hay en el curso
# calcular el promedio de los hombre

efmain():
    # Ingreso de la cantidad de alumnos
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos en el curso: "))
    
alumnos = []
cantidad_mujeres = 0
suma_notas_hombres = 0
cantidad_hombres = 0
    
for _ in range(cantidad_alumnos):
        # Ingreso de datos de cada alumno
        nombre = input("Ingrese el nombre del alumno: ")
        genero = input("Ingrese el género del alumno (hombre/mujer): ").strip().lower()
        nota1 = float(input("Ingrese la nota 1: "))
        nota2 = float(input("Ingrese la nota 2: "))
        nota3 = float(input("Ingrese la nota 3: "))
        
        # Cálculo del promedio de notas del alumno
        promedio = (nota1 + nota2 + nota3) / 3
        
        # Almacenamiento de los datos del alumno
        alumnos.append({
            'nombre': nombre,
            'genero': genero,
            'promedio': promedio
        })
        
        # Contar mujeres y acumular notas de hombres
        if genero == 'mujer':
            cantidad_mujeres += 1
        elif genero == 'hombre':
            suma_notas_hombres += promedio
            cantidad_hombres += 1
    
    # Mostrar promedios por alumno
for alumno in alumnos:
        print(f"Nombre: {alumno['nombre']}, Promedio: {alumno['promedio']:.2f}")
    
    # Calcular y mostrar el promedio de los hombres
if cantidad_hombres > 0:
        promedio_hombres = suma_notas_hombres / cantidad_hombres
        print(f"Cantidad de mujeres en el curso: {cantidad_mujeres}")
        print(f"Promedio de los hombres: {promedio_hombres:.2f}")
else:
        print(f"Cantidad de mujeres en el curso: {cantidad_mujeres}")
        print("No hay hombres en el curso.")

if __name__ == "__main__":
    main()