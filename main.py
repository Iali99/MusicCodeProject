import musicalbeeps
from FretBoard import FretBoardNotes
from MinorPentatonic import GetMinorPentatonicNotes


player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)

# Examples:
tempo = 120 #bpm
beatTime = 60/tempo #seconds

CSharpMinorPentatonic = GetMinorPentatonicNotes(9)

for note in CSharpMinorPentatonic:
    player.play_note(note, beatTime)
