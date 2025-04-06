import string

charClass = None
lexeme = []
nextChar = ''
lexLen = 0
token = None
nextToken = None
input_string = "(sum + 457) / total"
input_index = 0

LETTER = 0
DIGIT = 1
UNKNOWN = 99

INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = -1

def addChar():
    global lexLen
    if lexLen <= 98:
        lexeme.append(nextChar)
        lexLen += 1
    else:
        print("Error - lexeme is too long")

def getChar():
    global nextChar, charClass, input_index
    if input_index < len(input_string):
        nextChar = input_string[input_index]
        input_index += 1
    else:
        nextChar = ''
    
    if nextChar == '':
        charClass = EOF
    elif nextChar.isalpha():
        charClass = LETTER
    elif nextChar.isdigit():
        charClass = DIGIT
    else:
        charClass = UNKNOWN

def getNonBlank():
    while nextChar.isspace():
        getChar()

def lookup(ch):
    global nextToken
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF
    return nextToken

def lex():
    global lexLen, nextToken
    lexLen = 0
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()
        while charClass == LETTER or charClass == DIGIT:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme.append('E')
        lexeme.append('O')
        lexeme.append('F')

    print(f"Next token is: {nextToken}, Next lexeme is {''.join(lexeme)}")
    return nextToken

def main():
    getChar()
    while nextToken != EOF:
        lex()

if __name__ == "__main__":
    main()
