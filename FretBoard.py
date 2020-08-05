Notes  = ['A','A','B','C','C','D','D','E','F','F','G','G']
Sharps = ['','#','','','#','','#','','','#','','#']

def ConstructStringNotes(StartNote, Octave, frets):
    stringNotes = []
    octv = Octave
    for i in range(frets+1):
        pos = (StartNote + i)%12
        note = Notes[pos] + str(octv) + Sharps[pos]
        stringNotes.append(note)
        if pos == 2 :
            octv += 1

    return stringNotes

def GetFretBoardNotes(NoOfFrets):
    FretBoardNotes = []
    FretBoardNotes.append(ConstructStringNotes(7,3,NoOfFrets))
    FretBoardNotes.append(ConstructStringNotes(0,3,NoOfFrets))
    FretBoardNotes.append(ConstructStringNotes(5,4,NoOfFrets))
    FretBoardNotes.append(ConstructStringNotes(10,4,NoOfFrets))
    FretBoardNotes.append(ConstructStringNotes(2,4,NoOfFrets))
    FretBoardNotes.append(ConstructStringNotes(7,5,NoOfFrets))

    return FretBoardNotes

FretBoardNotes = GetFretBoardNotes(24)
