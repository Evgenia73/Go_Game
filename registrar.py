from typing import TextIO


class Registrar:
    def __init__(self):
        self.log: TextIO = open('history_of_moves.txt', "r+", encoding='UTF-8')
        self.log.truncate(0)
        self.log.write("История ходов:" + "\n")

    def write(self, txt: str):
        self.log.write(txt + "\n")

    def close(self):
        self.log.close()
