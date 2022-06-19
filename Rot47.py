class Rot47:
    def __init__(self):
        pass

    def pobierz_tekst(self):
        return input("Podaj tekst do zakodowania!")

    def koduj(self, txt):
        chars = []
        for char in range(len(txt)):
            unicode = ord(txt[char])
            if 33 <= unicode <= 126:
                chars.append(chr(33 + ((unicode + 14) % 94)))
            else:
                chars.append(txt[char])
        return "".join(chars)

    def dekoduj(self, txt):
        return self.koduj(txt)
