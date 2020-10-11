class ScaleGenarator():
    def __init__(self, key, scale):
        self.key = key
        self.scale = scale
        self.resultScale = []
        self.keysValue = { 
            0:'Ab',
            0.5:'A',
            1:'Bb',
            1.5:'B',
            2:'C',
            2.5:'Db',
            3:'D',
            3.5:'Eb',
            4:'E',
            4.5:'F',
            5:'Gb',
            5.5:'G' }

    def scaleGen(self):
        if self.scale == 'Major':
            return self.doMajor()
        elif self.scale == 'Minor':
            return self.doMinor()

    def doMajor(self):
        for note in self.keysValue:
            if self.keysValue[note] == self.key:
                counter = note
                for i in range(7):
                    if counter <= 4.5:
                        if i == 0:
                            self.resultScale.append(self.keysValue[counter])
                        elif i == 3:
                            counter+= 0.5
                            self.resultScale.append(self.keysValue[counter])
                        else:
                            counter+= 1
                            self.resultScale.append(self.keysValue[counter])
                    else:
                        if i == 0:
                            self.resultScale.append(self.keysValue[counter])
                        elif i == 3:                            
                            counter+= 0.5
                            if counter <= 5.5:
                                self.resultScale.append(self.keysValue[counter])
                            else:
                                self.resultScale.append(self.keysValue[counter-6])
                        else:
                            counter+= 1
                            self.resultScale.append(self.keysValue[counter-6])

        return self.resultScale

    def doMinor(self):
        for note in self.keysValue:
            if self.keysValue[note] == self.key:
                counter = note
                for i in range(7):
                    if counter <= 4.5:
                        if i == 0:
                            self.resultScale.append(self.keysValue[counter])
                        elif i == 2:
                            counter+= 0.5
                            self.resultScale.append(self.keysValue[counter])
                        elif i == 5:
                            counter+= 0.5
                            self.resultScale.append(self.keysValue[counter])
                        else:
                            counter+= 1
                            self.resultScale.append(self.keysValue[counter])
                    else:
                        if i == 0:
                            self.resultScale.append(self.keysValue[counter])
                        elif i == 2:                            
                            counter+= 0.5
                            if counter <= 5.5:
                                self.resultScale.append(self.keysValue[counter])
                            else:
                                self.resultScale.append(self.keysValue[counter-6])
                        elif i == 5:
                            counter+= 0.5
                            self.resultScale.append(self.keysValue[counter-6])
                        else:
                            counter+= 1
                            self.resultScale.append(self.keysValue[counter-6])

        return self.resultScale

 
                        

