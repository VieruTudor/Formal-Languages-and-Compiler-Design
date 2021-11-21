class FiniteAutomata:
    def __init__(self):
        self.Q = []
        self.E = []
        self.q0 = []
        self.F = []
        self.S = {}

        self.readFromFile("fa.in")

    def readFromFile(self, file):
        f = open(file)
        self.Q = f.readline().strip().split(' ')[2:]
        self.E = f.readline().strip().split(' ')[2:]
        self.q0 = f.readline().strip().split(' ')[2:]
        self.F = f.readline().strip().split(' ')[2:]

        parts = f.readline()[3:].strip().split(";")
        for x in parts:
            x = x.replace(' ', '')
            automataParts = x[1:-1].split(',')
            print(automataParts)
            source = automataParts[0]
            destination = automataParts[1]
            letter = automataParts[2]
            if (source, letter) not in self.S.keys():
                self.S[(source, letter)] = []
            self.S[(source, letter)].append(destination)
        print(self.S)

    def checkDFA(self):
        for key in self.S.keys():
            if len(self.S[key]) > 1:
                return False
        return True

    def isAccepted(self, sequence):
        if self.checkDFA():
            current = self.q0[0]
            for x in sequence:
                if (current, x) in self.S.keys():
                    current = self.S[(current, x)][0]
                else:
                    return False
            return current in self.F
        return False

    def printTransitions(self):
        for x in self.S:
            print(x[0] + '->' + x[1] + '(' + self.S[x][0] + ')')

