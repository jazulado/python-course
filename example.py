edadesEntre30y40 = 0
edadesEntre40y60 = 0
edadesMayor60 = 0
personas = 0
edades = 0
pesos = 0
while True:
    edad = float(input("Edad de la persona " + str(personas + 1) + ": "))
    peso = float(input("Peso de la persona " + str(personas + 1) + ": "))
    personas = personas+1
    edades = edades + edad
    pesos = pesos + peso
    if edad >= 30 and edad <= 40:
        edadesEntre30y40 = edadesEntre30y40 + 1
    if edad > 40 and edad <= 60:
        edadesEntre40y60 = edadesEntre40y60 + 1
    if edad > 60:
        edadesMayor60 = edadesMayor60 + 1
    if personas % 5 == 0:
        print("Llevas " + str(personas) + " personas encuestadas")
        ent = int(input("Ingresa 1 si quieres salir "))
        if ent == 1:
            break
print("edad promedio " + str(edades/personas))
print("peso promedio " +  str(pesos/personas))
print("personas entre 30 y 40 " + str(edadesEntre30y40))
print("personas entre 40 y 60 " + str(edadesEntre40y60))
print("personas mayores a 60 " + str(edadesMayor60))