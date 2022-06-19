class Menu:
    def __init__(self):
        pass

    def wyswietl_Menu(self):
        print(
            f" 1. Koduj rot13\n 2. Dekoduj rot13\n 3. Koduj Rot47\n 4. Dekoduj Rot47\n 5. Zakoncz"
        )

    def podaj_wybor(self):
        return int(input(f"Podaj jedna z opcji Menu!"))
