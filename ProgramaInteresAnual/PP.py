cantidad = float(input("�Cantidad a invertir? "))
interest = float(input("�Inter�s porcentual anual? "))
years = int(input("�A�os?"))
for i in range(years):
    cantidad *= 1 + interest / 100 
    print("Interes despu�s de " + str(i+1) + " a�os: " + str(round(cantidad, 2)))
