personas = int(input("ingrese numero de personas "))
total = 0
descuento = 0
propina = 0
for numpersona in range(1,personas+1):
    print("Persona " + str(numpersona) )
    print("Menu: [H]amburguesa, [P]erros, [S]alchipapa, [C]horizo o [0] Salir")
    eleccion = input("Seleccion: ")
    if eleccion == "h" or eleccion == "H":
        total = total + 10000
    
    elif eleccion == "p" or eleccion == "P":
        total = total + 8000
    
    elif eleccion == "s" or eleccion == "S":
        total = total + 6000
    elif eleccion == "c" or eleccion == "C":
        total = total + 7000
    elif eleccion == "0":
        break

hayprop = int(input("Desea incluir propina? [1]si [0]no: "))
if hayprop:
    propina = 0.1 * total

if total > 20000:
    descuento = total * 0.1
    print("Se realiza un descuento de 10% a su factura")

print("propina: " + str(propina))
print("descuento: " + str(descuento))
print("total: " + str(total + propina - descuento))