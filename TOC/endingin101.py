## dfa for language endig in 101
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
            if (char not in self.symbols):
                print(f"Symbol {char} is not in input set")
                return
            self.current = self.transitions[self.current][char]
        if self.current in self.final:
            print("Accepted")
        else:
            print("Invalid")
tr = {0: {'0': 0, '1': 1},
      1: {'0': 2, '1': 1},
      2: {'0': 0, '1': 3},
      3: {'0': 2, '1': 1}}
d = dfa(tr, ('0', '1'), (3,))
inp = input("Enter the string: ")
d.check(inp)