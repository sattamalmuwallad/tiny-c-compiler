class Lexer:
    def __init__(self, source):
        self.source = source + "\n"
        self.curchar = ""
        self.curpos = -1
        self.nextChar()
        

    # Process the next character.
    def nextChar(self):
        self.curpos +=1
        if self.curpos >= len(self.source):
            self.curchar = "\0"
        else:
            self.curchar = self.source[self.curpos] 

    # Return the lookahead character.
    def peek(self):
        pass

    # Invalid token found, print error message and exit.
    def abort(self, message):
        pass
		
    # Skip whitespace except newlines, which we will use to indicate the end of a statement.
    def skipWhitespace(self):
        pass
		
    # Skip comments in the code.
    def skipComment(self):
        pass

    # Return the next token.
    def getToken(self):
        pass
    