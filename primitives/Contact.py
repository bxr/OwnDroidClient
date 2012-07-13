class Contact:
    def __init__(self,name="", numbers=[]  ):
        self.name=name;
        self.numbers=numbers
        
    def getName( self ):
        return self.name
    
    def getNumbers( self ):
        return self.numbers