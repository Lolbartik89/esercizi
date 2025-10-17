def calculator():

    print("Calcolatrice semplice")

    num1 = float(input("Inserisci il primo numero"))
    operazione = input("Scgeli operazione:(+, -, /, *).")
    num2 = float(input("Inserisci il secondo numero"))

    if operazione == '+':
        print("Resultato:", num1 + num2)
    elif operazione == '-':
        print("Resultato:", num1 - num2)
    elif operazione == '*':
        print("Resultato:", num1 * num2)
    elif operazione == '/':
        if num2 != 0:
            print("Resultato:", num1 / num2)
        else:
            print("Errore")
    else:
        print("Operazione sconosciuta")

calculator()