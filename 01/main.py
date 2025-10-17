def calculator():
    while True:

        print("Calcolatrice semplice")

        num1 = float(input("Inserisci il primo numero: "))
        operazione = input("Scegli operazione (+, -, /, *): ")
        num2 = float(input("Inserisci il secondo numero: "))

        if operazione == "+":
            print("Risultato:", num1 + num2)
        elif operazione == "-":
            print("Risultato:", num1 - num2)
        elif operazione == "*":
            print("Risultato:", num1 * num2)
        elif operazione == "/":
            if num2 != 0:
                print("Risultato:", num1 / num2)
            else:
                print("Errore: divisione per zero")
        else:
            print("Operazione sconosciuta")
            continue

        again = input("Vuoi continuare? (si/no): ").lower()
        if again != "si":
            print("Ciao")
            break

calculator()
