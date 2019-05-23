import mido

from .instrument import Instrument


class Listener:
    def __init__(self):
        self.devices = mido.get_input_names()
        self.device = self.devices[0]

    def connect(self):
        """Connect to midi input device"""
        self.port = mido.open_input(self.device)

    def listen(self, instrument: Instrument):
        """Listen for messages from midi input device"""
        try:
            msg = self.port.receive()

            for msg in self.port:
                signal = msg.type
                pitch = msg.note
                print(signal, " ", pitch)
                if signal == "note_on":
                    string = instrument.select_string(pitch, play=True)
                    fret = string.notes.index(pitch)
                    string.play(fret)
                if signal == "note_off":
                    string = instrument.select_string(pitch, play=False)
                    string.release(fret)

        except KeyboardInterrupt:
            self.port.close()
