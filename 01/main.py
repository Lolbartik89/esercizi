def inputCheck(value):
    value = str(value).strip()
    value = value.replace(",", ".")
    try:
        return float(value)
    except ValueError:
        print(f"Errore: '{value}' non è un numero valido!")
        return None  # Возвращаем None, если не число

def calculator():
    while True:
        print("\n--- Calcolatrice semplice ---")

        num1 = None
        while num1 is None:  # Повторяем ввод пока число не будет валидным
            num1 = inputCheck(input("Inserisci il primo numero: "))

        operazione = input("Scegli operazione (+, -, /, *): ")

        num2 = None
        while num2 is None:
            num2 = inputCheck(input("Inserisci il secondo numero: "))

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
                print("Errore: divisione per zero!")
        else:
            print("Operazione sconosciuta, riprova...")
            continue

        again = input("Vuoi continuare? (si/no): ").lower()
        if again != "si":
            print("Ciao!")
            break

calculator()

