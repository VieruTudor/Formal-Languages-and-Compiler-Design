import re

from symbol import SymbolTable

from regex import *


class Scanner:
    def __init__(self, programFile, tokenFile):
        self.tokenFile = tokenFile
        self.programFile = programFile
        self.reserved = []
        self.separators = ['(', ')', '{', '}', ' ', ',', ':', '\n']
        self.operators = []

        self.parseReserved()

    def parseReserved(self):
        f = open(self.tokenFile)
        for line in f:
            line = line.strip()
            if re.match(r'[a-zA-Z]', line):
                self.reserved.append(line)
            else:
                self.operators.append(line)

    def isIdentifier(self, token):
        return re.match(r'^[_a-zA-Z]([_a-zA-Z0-9])*$', token)

    def isConstant(self, token):
        return isChar(token) or isNumber(token) or isString(token)

    def scan(self):
        f = open(self.programFile)
        for line in f:
            self.ParseTokensInLine(line.strip())
            pass

    def isInOperator(self, char):
        for res in self.operators:
            if char in res:
                return True
        return False

    def getCharToken(self, line, index):
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '\'':
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    def getOperatorToken(self, line, index):
        token = ''
        while index < len(line) and self.isInOperator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def getStringToken(self, line, index):
        token = ''
        quotes = 0
        while index < len(line) and quotes < 2:
            if line[index] == '\"':
                quotes += 1
            token += line[index]
            index += 1
        return token, index

    def ParseTokensInLine(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            # is char
            if line[index] == '\'':
                if token:
                    tokens.append(token)
                else:
                    token, index = self.getCharToken(line, index)
                    tokens.append(token)
                    token = ''
            # is string
            elif line[index].strip() == '\"':
                if token:
                    tokens.append(token)
                token, index = self.getStringToken(line, index)
                tokens.append(token)
                token = ''

            elif self.isInOperator(line[index]):
                if token:
                    tokens.append(token)

                token, index = self.getOperatorToken(line, index)
                tokens.append(token)
                token = ''

            elif line[index] in self.separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                # print(token)
                tokens.append(token)
                token = ''

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)

        tokens = [x for x in tokens if x != ' ']
        # print(tokens)
        return tokens



