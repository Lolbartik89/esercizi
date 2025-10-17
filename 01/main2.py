#Gestore di liste della spesa
def load_list(filename):
    try:
        with open (filename, "r") as file:
            return[line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return[]
def save_list(filename, shopping_list):
    with open(filename, "w") as file:
        for item in shopping_list:
            file.write(item + "\n")
def add_item(shopping_list):
    item = input("Inserisci un prodotto da aggiungere:")
    shopping_list.append(item)
    print(f'{item} aggiunto alla lista')
def remove_item(shopping_list):
    item = input("inserisci il prodotto da rimuovere:")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'"{item}" rimosso dalla lista.')
    else:
        print(f'"{item}" non trovato nella lista.')
def show_list(shopping_list):
    if not shopping_list:
        print("La lista vuota.")
    else:
        print("Lista della spesa:")
        for i, item in enumerate(shopping_list, start=1):
            print({f"{i}. {item}"})
def main():
    filename = "lista_spesa.txt"
    shopping_list = load_list(filename)
    while True:
        print("-Menu-")
        print("1.Mostra la lista")
        print("2.Aggiungi un prodotto")
        print("3. Rimuovi un prodotto")
        print("4. Exit")
        choice = input("Scegli un operazioe (1-4):")

        if choice == "1":
            show_list(shopping_list)
        elif choice == "2":
            add_item(shopping_list)
            save_list(filename, shopping_list)
        elif choice == "3":
            remove_item(shopping_list)
            save_list(filename, shopping_list)
        elif choice == "4":
            print("Uscita dal programma. CIAO!")
            break  # noqa: F701
        else:
            print("Opzione non valida.")
if __name__ == "__main__":
    main()

