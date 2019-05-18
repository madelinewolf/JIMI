from .data.note_values import note_values


class Note:
    def __init__(self, midi_value: int):
        self.midi = midi_value
        self.name = note_values.get(midi_value)
        self.octave = self.name[-1]
        if len(self.name) == 3:
            self.value = self.name[0:2]
        else:
            self.value = self.name[0]
