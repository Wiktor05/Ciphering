class File:
    def __init__(self):
        pass

    def type_filename(self):
        return input("Type in a file name: ")

    def save_to_file(self, txt, filename):
        with open(filename, "w") as file:
            file.write(txt)

    def read_from_file(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()

        return " ".join(lines)
