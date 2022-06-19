class Rot13:
    def __init__(self):
        pass

    def pobierz_tekst(self):
        return input("Podaj tekst do zakodowania: ")

    def koduj(self, txt):
        chars = []
        for char in range(len(txt)):
            unicode = ord(txt[char])
            if 97 <= unicode <= 122:
                chars.append(chr((unicode - 84) % 26 + 97))
            elif 65 <= unicode <= 90:
                chars.append(chr((unicode - 52) % 26 + 65))
            else:
                chars.append(txt[char])
        return "".join(chars)

    def dekoduj(self, txt):
        return self.koduj(txt)
