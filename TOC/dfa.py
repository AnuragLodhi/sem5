## dfs for language ending with a
class dfa:
    def __init__(self, transitions):
        self.symbols = ('a', 'b')
        self.current = 0
        self.initial = 0
        self.final = (1,)
        self.transitions = transitions
    
    def check(self, inp):
        self.current = self.initial
        for char in inp:
            self.current = self.transitions[self.current][char]
        if self.current in self.final:
            print("Accepted")
        else:
            print("Invalid")

tr = {0: {'a': 1, 'b': 0}, 1: {'a': 1, 'b': 0}}
tr2 = {0: {'a': 1, 'b': 0}, 1: {'a': 0, 'b': 1}}
endsInA = dfa(tr)
oddA = dfa(tr2)
inp = input("Enter the string: ")
endsInA.check(inp)
oddA.check(inp)