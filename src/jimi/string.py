from .note import Note


class String:
    def __init__(self, order: int, frets: int):
        self.order = order
        self.frets = frets
        self.lowest_note = int
        self.highest_note = int
        self.notes = []

    def get_notes(self, lowest_note: int):
        self.lowest_note = lowest_note
        self.highest_note = lowest_note + self.frets

        for note in range(self.lowest_note, self.highest_note + 1):
            self.notes.append(Note(note))
