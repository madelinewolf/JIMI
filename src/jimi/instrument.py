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

    def select_string(self, pitch: int, play: bool = True) -> String:
        """Select string to play a note"""
        for string in self.strings:
            if play:
                if pitch in string.notes and string.is_available:
                    return string
            else:
                if pitch in string.notes and not string.is_available:
                    return string
