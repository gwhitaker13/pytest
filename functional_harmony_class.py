class functional_harmony(object):

    def __init__(self):
        '''
        create note universe
        '''
        self.notes = {1:'C',2:'D',3:'E',4:'F',5:'G',6:'A',7:'B'}
        self.key = 'C'
        
    def Ichord(self):
        '''
        Tonic
        '''
        root = list(self.notes.keys())[list(self.notes.values()).index(self.key)]
        
        if root + 2 <= 7:
            third = root + 2
        else:
            third = root - 5
            
        if third + 2 <= 7:
            fifth = third + 2
        else:
            fifth = third - 5
            
        for n in [root, third, fifth]:
            print (self.notes[n])
            
    def iichord(self):
        '''
        Super-tonic
        '''
        key = list(self.notes.keys())[list(self.notes.values()).index(self.key)]
        
        if key + 1 <= 7:
            root = key + 1
        else:
            root = key - 6
        
        if root + 2 <= 7:
            third = root + 2
        else:
            third = root - 5
            
        if third + 2 <= 7:
            fifth = third + 2
        else:
            fifth = third - 5
            
        for n in [root, third, fifth]:
            print (self.notes[n].lower())
            
    def iiichord(self):
        '''
        Mediant
        '''
        key = list(self.notes.keys())[list(self.notes.values()).index(self.key)]
        
        if key + 2 <= 7:
            root = key + 2
        else:
            root = key - 5
        
        if root + 2 <= 7:
            third = root + 2
        else:
            third = root - 5
            
        if third + 2 <= 7:
            fifth = third + 2
        else:
            fifth = third - 5
            
        for n in [root, third, fifth]:
            print (self.notes[n].lower())

    def IVchord(self):
        '''
        Sub-dominant
        '''
        key = list(self.notes.keys())[list(self.notes.values()).index(self.key)]
        
        if key + 3 <= 7:
            root = key + 3
        else:
            root = key - 4
        
        if root + 2 <= 7:
            third = root + 2
        else:
            third = root - 5
            
        if third + 2 <= 7:
            fifth = third + 2
        else:
            fifth = third - 5
            
        for n in [root, third, fifth]:
            print (self.notes[n])
        
    def Vchord(self):
        '''
        Dominant
        '''
        key = list(self.notes.keys())[list(self.notes.values()).index(self.key)]
        
        if key + 4 <= 7:
            root = key + 4
        else:
            root = key - 3
        
        if root + 2 <= 7:
            third = root + 2
        else:
            third = root - 5
            
        if third + 2 <= 7:
            fifth = third + 2
        else:
            fifth = third - 5
            
        for n in [root, third, fifth]:
            print (self.notes[n])
            
    def vichord(self):
        '''
        Sub-mediant
        '''
        key = list(self.notes.keys())[list(self.notes.values()).index(self.key)]
        
        if key + 5 <= 7:
            root = key + 5
        else:
            root = key - 2
        
        if root + 2 <= 7:
            third = root + 2
        else:
            third = root - 5
            
        if third + 2 <= 7:
            fifth = third + 2
        else:
            fifth = third - 5
            
        for n in [root, third, fifth]:
            print (self.notes[n].lower())
            
    def viichord(self):
        '''
        Leading diminished
        '''
        key = list(self.notes.keys())[list(self.notes.values()).index(self.key)]
        
        if key + 6 <= 7:
            root = key + 6
        else:
            root = key - 1
        
        if root + 2 <= 7:
            third = root + 2
        else:
            third = root - 5
            
        if third + 2 <= 7:
            fifth = third + 2
        else:
            fifth = third - 5
            
        for n in [root, third, fifth]:
            print (self.notes[n].lower())