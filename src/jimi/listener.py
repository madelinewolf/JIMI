import mido


class listener:
    def __init__(self):
        self.devices = mido.get_input_names()
        self.device = self.devices[0]

    def connect(self):
        """Connect to midi input device"""
        self.port = mido.open_input(self.device)

    def listen(self):
        """Listen for messages from midi input device"""
        try:
            msg = self.port.receive()

            for msg in self.port:
                signal = msg.type
                pitch = msg.note
                print(signal, " ", pitch)
        except KeyboardInterrupt:
            self.port.close()
