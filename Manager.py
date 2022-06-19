from Menu import Menu
from Rot13 import Rot13
from FileHandler import FileHandler
from Rot47 import Rot47


class Menager:
    def __init__(self):
        self.menu = Menu()
        self.rot13 = Rot13()
        self.rot47 = Rot47
        self.file_handler = FileHandler()

        self.is_running = True
        self.options = {
            1: self.__do_opt1,
            2: self.__do_opt2,
            3: self.__do_opt3,
            4: self.__do_opt4,
            5: self.__exit_app,
        }

    def display_start(self):
        print(f"Start")
        self.menu.wyswietl_Menu()
        while self.is_running:
            wybor = self.menu.podaj_wybor()
            self.podejmij_dzialanie(wybor)

    def __exit_app(self):
        self.is_running = False

    def __do_opt1(self):
        txt = self.rot13.pobierz_tekst()
        filename = self.file_handler.type_filename()

        encrypted_txt = self.rot13.koduj(txt)
        self.file_handler.save_to_file(encrypted_txt, filename)
        print(f"Saving has finished!, wynik to: {encrypted_txt}")

    def __do_opt2(self):
        filename = input(f" Please, write filename!")
        encrypted_txt = self.file_handler.read_from_file(filename)
        print(self.rot13.dekoduj(encrypted_txt))

    def __do_opt3(self):
        txt = self.rot47.pobierz_tekst()
        filename = self.file_handler.type_filename()

        encrypted_txt = self.rot13.koduj(txt)
        self.file_handler.save_to_file(encrypted_txt, filename)
        print(f"Saving has finished!, wynik to: {encrypted_txt}")

    def __do_opt4(self):
        filename = input(f" Please, write filename!")
        encrypted_txt = self.file_handler.read_from_file(filename)
        print(self.rot47.dekoduj(encrypted_txt))

    def show_error(self):
        print("Invalid input!")

    def podejmij_dzialanie(self, wybor):
        self.options.get(wybor, self.show_error)()
