from Part import Part
from itertools import product


class Sequence(object):

    seq = []

    def __init__(self, digitList):
        # str = -(1)+(2)+(3)...
        for ndx, val in enumerate(digitList):
            if ndx == 0:
                self.seq.append(Part(Part.NEG))

            if ndx > 0:
                self.seq.append(Part(Part.OP))

            if ndx < len(digitList) - 1:
                self.seq.append(Part(Part.PRE))

            self.seq.append(Part(Part.DIG, val))

            if ndx > 1:
                self.seq.append(Part(Part.POST))

    def __iter__(self):
        allSequences = product(*self.seq)
        for x in allSequences:
            expression = ''.join(x)
            if self.hasValidParens(expression) and self.isCalculatable(expression):
                yield expression

    def hasValidParens(self, exp):
        if exp.count('(') != exp.count(')'):
            return False

        unmatched = 0
        for char in exp:
            if char == '(':
                unmatched += 1
            elif char == ')':
                if unmatched == 0:
                    return False
                unmatched -= 1

        return True

    def isCalculatable(self, exp):
        return exp.count('**') < 2
