class ChordsGenarator():
    def __init__(self,scale,notesList):
        self.scale = scale
        self.notesList = notesList
        self.chordsList = []

    def genChords(self):
        if self.scale == 'Minor':
            return self.genMinor()
        elif self.scale == 'Major':
            return self.genMajor()
    
    def genMinor(self):
        for i in range(7):
            if i == 1:
                self.chordsList.append(self.notesList[i]+'dim')
            elif i == 2 or i == 5 or i== 6:
                self.chordsList.append(self.notesList[i])
            else:
                self.chordsList.append(self.notesList[i]+'m')
        return self.chordsList
        
    def genMajor(self):
        for i in range(7):
            if i == 6:
                self.chordsList.append(self.notesList[i]+'dim')
            elif i == 0 or i == 3 or i== 4:
                self.chordsList.append(self.notesList[i])
            else:
                self.chordsList.append(self.notesList[i]+'m')
        return self.chordsList

