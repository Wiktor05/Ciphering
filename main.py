from Manager import Menager


def main():
    manager = Menager()
    manager.display_start()


if __name__ == "__main__":
    main()

#
# class Human:
#     def __init__(self, name):
#         self.name = name
#
#     def __show(self):
#         print("HI!")
#
#     def show2(self):
#         self.__show()
#
# human = Human("Wiktor")
# print(human.name)
# human.__show()