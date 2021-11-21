from scanner import Scanner
from symbol import SymbolTable, HashTable


def main():
    programFile = "p1.txt"
    tokenFile = "token.in"
    outputPIF = "pif.out"
    outputST = "st.out"
    symbolTable = SymbolTable(6)
    PIF = []
    scanner = Scanner(programFile, tokenFile)

    f = open(programFile)

    lineNumber = 0

    for line in f:
        lineNumber += 1
        for token in scanner.ParseTokensInLine(line):
            if token in scanner.reserved + scanner.operators + scanner.separators:
                if token == ' ' or token == '\n':
                    continue
                PIF.append((token, (-1, -1)))
            elif scanner.isIdentifier(token):
                pos = symbolTable.insert(token)
                PIF.append(("identifier", pos))
            elif scanner.isConstant(token):
                pos = symbolTable.insert(token)
                PIF.append(("constant", pos))
            else:
                print("Error on line: ", lineNumber)

    filePIF = open(outputPIF, 'w')
    fileST = open(outputST, 'w')

    for x in PIF:
        line = str(x[0]) + ' -> ' + str(x[1])
        filePIF.write(line + "\n")

    for x in range(0, symbolTable.hashtable.capacity):
        fileST.write(str(x) + " : ")
        fileST.write(' '.join(str(item) for item in symbolTable.hashtable.table[x]))
        fileST.write("\n")

main()