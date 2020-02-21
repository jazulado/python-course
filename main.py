promedio = float(input("ingrese su promedio "))
modalidad = "pregrado"
creditos = 0
descuento = 0
podraMatricular = 1

if modalidad == "pregrado":
    if promedio >= 4.5:
        creditos = 28
        descuento = 0.25
    elif promedio < 4.5 and promedio >= 4:
        creditos = 25
        descuento = 0.1
    elif promedio < 4 and promedio >= 3.5:
        creditos = 20
        descuento = 0
    elif promedio < 3.5 and promedio >= 2.5:
        creditos = 15
        descuento = 0
    elif promedio < 2.5:
        print("no podra matricularse")
        podraMatricular = 0
else:
    if promedio >= 4.5:
        creditos = 20
        descuento = 0.2
    elif promedio < 4.5 and promedio >= 0:
        creditos = 10
        descuento = 0
        
if podraMatricular == 1:
    if modalidad == "pregrado":
        print("creditos: " + str(creditos) + " total a pagar: " + str(creditos* 50000))
        print("descuento: " + str((creditos*50000)*descuento) + " total con adescuento: " + str((creditos*50000)*(1-descuento)))
    if modalidad == "posgrado":
        print("creditos: " + str(creditos) + " total a pagar: " + str(creditos* 300000))
        print("descuento: " + str((creditos*300000)*descuento) + " total con descuento: " + str((creditos*300000)*(1-descuento)))