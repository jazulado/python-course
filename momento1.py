print("Proceso de finalizacion de semestre")
numalumnos = int(input("Ingrese el numero de alumnos "))
numhombres = 0
nummujeres = 0

for alumno in range(1,numalumnos+1):
    notaac = 0
    programa = input("Ingrese el programa academico ")
    genero = str(input("Ingrese [m]ujer o [h]ombre "))
    if genero == "m":
        nummujeres = nummujeres + 1
    elif genero == "h":
        numhombres = numhombres + 1
    for nota in range(1,6):
        notaac = float(input("ingrese la nota " + str(nota) + ": ")) + notaac
    print("El promedio de la nota es: " + str(notaac / 5.0))

print("El numero de mujeres es: " + str(nummujeres )+" y el numero de hombres es: " + str(numhombres ))

print("Proceso de admision")

numalumno = 0
counter = 1
numhombres = 0
nummujeres = 0
edades = 0
while counter != 0:
    edades = int(input("Ingrese la edad de el " + str(numalumno) + " para matricularse "))  + edades
    genero = str(input("Ingrese [m]ujer o [h]ombre del " + str(numalumno) + " alumno "))
    if genero == "m":
        nummujeres = nummujeres + 1
    elif genero == "h":
        numhombres = numhombres + 1
    numalumno  = 1 + numalumno 
    counter = int(input("Ingresa 0 si quieres salir o 1 si no "))
print("El promedio de las edades es " + str(float(edades) / float(numalumno)))
print("El numero de mujeres es: " + str(nummujeres )+" y el numero de hombres es: " + str(numhombres ))