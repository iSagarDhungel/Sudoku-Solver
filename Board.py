class Board:
    '''
    Class for the Sudoku Board and Its CSP
    '''
    def __init__(self, string):
        '''
        Takes initial Board Position as Argument
        Initialises Board and CSP for given Board State
        '''
        self.Keys = [['A1','A2','A3','A4','A5','A6','A7','A8','A9'],
                     ['B1','B2','B3','B4','B5','B6','B7','B8','B9'],
                     ['C1','C2','C3','C4','C5','C6','C7','C8','C9'],
                     ['D1','D2','D3','D4','D5','D6','D7','D8','D9'],
                     ['E1','E2','E3','E4','E5','E6','E7','E8','E9'],
                     ['F1','F2','F3','F4','F5','F6','F7','F8','F9'],
                     ['G1','G2','G3','G4','G5','G6','G7','G8','G9'],
                     ['H1','H2','H3','H4','H5','H6','H7','H8','H9'],
                     ['I1','I2','I3','I4','I5','I6','I7','I8','I9']]
        
        self.Combinations = [['A1','B1','C1','D1','E1','F1','G1','H1','I1'],
                             ['A2','B2','C2','D2','E2','F2','G2','H2','I2'],
                             ['A3','B3','C3','D3','E3','F3','G3','H3','I3'],
                             ['A4','B4','C4','D4','E4','F4','G4','H4','I4'],
                             ['A5','B5','C5','D5','E5','F5','G5','H5','I5'],
                             ['A6','B6','C6','D6','E6','F6','G6','H6','I6'],
                             ['A7','B7','C7','D7','E7','F7','G7','H7','I7'],
                             ['A8','B8','C8','D8','E8','F8','G8','H8','I8'],
                             ['A9','B9','C9','D9','E9','F9','G9','H9','I9'],
                             ['A1','A2','A3','B1','B2','B3','C1','C2','C3'],
                             ['D1','D2','D3','E1','E2','E3','F1','F2','F3'],
                             ['G1','G2','G3','H1','H2','H3','I1','I2','I3'],
                             ['A4','A5','A6','B4','B5','B6','C4','C5','C6'],
                             ['D4','D5','D6','E4','E5','E6','F4','F5','F6'],
                             ['G4','G5','G6','H4','H5','H6','I4','I5','I6'],
                             ['A7','A8','A9','B7','B8','B9','C7','C8','C9'],
                             ['D7','D8','D9','E7','E8','E9','F7','F8','F9'],
                             ['G7','G8','G9','H7','H8','H9','I7','I8','I9'],
                             ['A1','A2','A3','A4','A5','A6','A7','A8','A9'],
                             ['B1','B2','B3','B4','B5','B6','B7','B8','B9'],
                             ['C1','C2','C3','C4','C5','C6','C7','C8','C9'],
                             ['D1','D2','D3','D4','D5','D6','D7','D8','D9'],
                             ['E1','E2','E3','E4','E5','E6','E7','E8','E9'],
                             ['F1','F2','F3','F4','F5','F6','F7','F8','F9'],
                             ['G1','G2','G3','G4','G5','G6','G7','G8','G9'],
                             ['H1','H2','H3','H4','H5','H6','H7','H8','H9'],
                             ['I1','I2','I3','I4','I5','I6','I7','I8','I9']]
        
        self.FlatKeys = tuple(sum(self.Keys,[]))
        
        Values = list(string[i:i+1] for i in range(len(string)))
        self.BoardState = dict(zip(self.FlatKeys,Values))
        self.Domain = dict.fromkeys(self.FlatKeys,None)
        self.TileState = dict.fromkeys(self.FlatKeys,None)
        
        for Key in self.FlatKeys:
            if self.BoardState[Key] == '0':
                self.Domain[Key] = ['1','2','3','4','5','6','7','8','9']
                self.TileState[Key] = False
            else:
                self.Domain[Key] = [self.BoardState[Key]]
                self.TileState[Key] = True
    
        for Key in self.FlatKeys:
            self.UpdateDomain(Key)

    def UpdateDomain(self,Key):
        '''
        returns True for variables with non- empty domains.
        '''
        if self.TileState[Key]:
            return True
        
        InvalidValues = set('0')
        for Combination in self.Combinations:
            if Key in Combination:
                for x in Combination:
                    InvalidValues.add(self.BoardState[x])
        
        DomainValues = ['1','2','3','4','5','6','7','8','9']
        #remove 0 as they imply empty placeholder
        InvalidValues.remove('0')
        for i in InvalidValues:
            DomainValues.remove(i)

        self.Domain[Key] = DomainValues
        return bool(self.Domain[Key])
            

    def GetUnassignedVariable(self):
        '''
        returns Unassigned variable according to MRV
        '''
        
        UnassignedKey = None 
        LenKey   = 10
        for Key in self.FlatKeys:
            if  not self.TileState[Key]:
                if len(self.Domain[Key]) < LenKey:
                    UnassignedKey = Key
                    LenKey = len(self.Domain[Key])
                
        return UnassignedKey

    def Assign(self, Key, Value):
        '''
        Assigns a value to variable and updates the board State
        '''
        self.BoardState[Key] = Value
        self.Domain[Key] = [Value]
        self.TileState[Key] = True
        for Key in self.FlatKeys:
            self.UpdateDomain(Key)
    
    
    def UnAssign(self, Key):
        '''
        Assigns a value to variable and updates the board State
        '''
        self.BoardState[Key] = '0'
        self.TileState[Key] = False
        for Key in self.FlatKeys:
            self.UpdateDomain(Key)
    
    def DisplayBoardOnly(self):
        print("\n  1 2 3 4 5 6 7 8 9\n")
        for Key in self.Keys:
            print(Key[0][0] , end = ' ')
            for K in Key:
                print(self.BoardState[K], end = ' ')
            print('')
    
    def ShowBoardState(self):
        self.DisplayBoardOnly();
        for Key in self.FlatKeys:
            print(Key, self.BoardState[Key],self.TileState[Key], self.Domain[Key])
            

    
    def CheckConsistency(self,Key):
        '''
        Check for consistency of the board
        Returns True if consistent
        '''
        j = 0
        CheckedBoardState = set()
        for x in self.Combinations:
            if Key in x:
                
                j += 1
                for i in x:
                    if ( self.TileState[i] ):
                        if i == Key:
                            continue
                        CheckedBoardState.add(self.BoardState[i])
                        
        if self.BoardState[Key] in CheckedBoardState:
          
            return False                  
        return True
    
    def IsComplete(self):
        '''
        Returns true if all assignment is done
        '''
        for Key in self.FlatKeys: 
            if  not self.TileState[Key]:   
                return False
        return True
    
    def WriteOutput(self):
        if not self.IsComplete():
            return 'Incomplete'
        Output = ''
        for Key in self.FlatKeys:
            Output += self.BoardState[Key]
        return Output
        
        
def BackTrack(CSP):
    '''
    Returns True if solution was found
    '''
    if CSP.IsComplete():
        return True
    
    Variable = CSP.GetUnassignedVariable()
    
    Values = CSP.Domain[Variable]
    
    for Value in Values:    
        Result = False;
        CSP.Assign(Variable,Value)    
        if CSP.CheckConsistency(Variable):
            Result = BackTrack(CSP)
            if Result :
                return True
        CSP.UnAssign(Variable)
        
    return False