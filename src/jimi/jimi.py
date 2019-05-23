from .instrument import Instrument
from .listener import Listener


uke = Instrument(4, 4)

uke.strings[0].get_notes(67)  # G4 string
uke.strings[1].get_notes(60)  # C4 string
uke.strings[2].get_notes(64)  # E4 string
uke.strings[3].get_notes(69)  # A4 string

listener = Listener()
listener.connect()
listener.listen(uke)
