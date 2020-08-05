from FretBoard import FretBoardNotes

def GetMinorPentatonicNotes(StartFret):
    pentatonicNotes = []
    pentatonicNotes.append(FretBoardNotes[0][StartFret])
    pentatonicNotes.append(FretBoardNotes[0][StartFret+3])
    pentatonicNotes.append(FretBoardNotes[1][StartFret])
    pentatonicNotes.append(FretBoardNotes[1][StartFret+2])
    pentatonicNotes.append(FretBoardNotes[2][StartFret])
    pentatonicNotes.append(FretBoardNotes[2][StartFret+2])
    pentatonicNotes.append(FretBoardNotes[3][StartFret])
    pentatonicNotes.append(FretBoardNotes[3][StartFret+2])
    pentatonicNotes.append(FretBoardNotes[4][StartFret])
    pentatonicNotes.append(FretBoardNotes[4][StartFret+3])
    pentatonicNotes.append(FretBoardNotes[5][StartFret])
    pentatonicNotes.append(FretBoardNotes[5][StartFret+3])

    return pentatonicNotes
