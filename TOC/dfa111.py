## dfa for language containing substring '111'
class dfa:
    def __init__(self, transitions, symbols, final):
        self.symbols = symbols
        self.current = 0
        self.initial = 0
        self.final = final
        self.transitions = transitions
    
    def check(self, inp):
        self.current = self.initial
        for char in inp:
            self.current = self.transitions[self.current][char]
        if self.current in self.final:
            print("Accepted")
        else:
            print("Invalid")

tr111 = {0: {'0': 0, '1': 1},
         1: {'0': 0, '1': 2},
         2: {'0': 0, '1': 3},
         3: {'0': 3, '1': 3}}
threeone = dfa(tr111, ('0', '1'), (3,))
inp = input("Enter the string: ")
threeone.check(inp)