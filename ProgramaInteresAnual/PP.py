cantidad = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    cantidad *= 1 + interest / 100 
    print("Interes después de " + str(i+1) + " años: " + str(round(cantidad, 2)))
