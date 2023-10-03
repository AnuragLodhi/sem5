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

tr = {0: {'a': 1, 'b': 1}, 1: {'a': 0, 'b': 0}}
d = dfa(tr, ('a', 'b'), (0,))
inp = input("Enter string: ")
d.check(inp)