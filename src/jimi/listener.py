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
                if pitch in instrument.range:
                    if signal == "note_on":
                        string = instrument.select_string(pitch, play=True)
                        print(string)
                        fret = string.notes.index(pitch)
                        print(fret)
                        string.play(fret)
                    if signal == "note_off":
                        string = instrument.select_string(pitch, play=False)
                        print(string)
                        fret = string.notes.index(pitch)
                        print(fret)
                        string.release(fret)
                else:
                    print(
                        f"Pitch out of range.  Instrument range is {instrument.lowest_note} to {instrument.highest_note}"
                    )

        except KeyboardInterrupt:
            self.port.close()

        finally:
            self.port.close()
