from FiniteAutomata import FiniteAutomata


def printMenu():
    print("1. Read from file\n"
          "2. Display set of states\n"
          "3. Display the alphabet\n"
          "4. Display all transitions\n"
          "5. Display final states\n"
          "6. Display if it is DFA\n"
          "7. Check if sequence is accepted by the DFA")


fa = FiniteAutomata()
while True:
    printMenu()
    choice = input(">>>")
    if choice == '1':
        fa.readFromFile("fa.in")
    if choice == '2':
        print(fa.Q)
    if choice == '3':
        print(fa.E)
    if choice == '4':
        fa.printTransitions()
    if choice == '5':
        print(fa.F)
    if choice == '6':
        print(fa.checkDFA())
    if choice == '7':
        sequence = input("input sequence:")
        print(fa.isAccepted(sequence))