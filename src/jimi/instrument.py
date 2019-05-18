from .string import String


class Instrument:
    def __init__(self, strings: int, frets: int):
        self.num_strings = strings
        self.frets = frets
        self.strings = []
        self.create_strings()

    def create_strings(self):
        for i in range(self.num_strings):
            self.strings.append(String(i, self.frets))
