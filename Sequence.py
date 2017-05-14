from part.neg import Neg
from part.op import Op
from part.pre import Pre
from part.post import Post
from part.number import Number
from itertools import product
from functools import reduce


class Sequence:
    seq = []

    def __init__(self, digitList, staticParts=0, segment=0):
        super(Sequence).__init__()
        # -(1)+(2)+(3)...
        for ndx, val in enumerate(digitList):
            if ndx == 0:
                self.addToSequence(Neg())
            if ndx > 0:
                self.addToSequence(Op())

            if ndx < len(digitList) - 1:
                self.addToSequence(Pre())
            self.addToSequence(Number(val))
            if ndx > 1:
                self.addToSequence(Post())

        staticSection = self.seq[:staticParts]
        segments = reduce(lambda x, y: x * y.length(), staticSection, 1)
        print('Test set broken into %d segments' % segments)

        if segment >= segments:
            print('Segment number out of bounds')
            raise IndexError

        for section in staticSection:
            v = segment % section.length()
            section.lock(v)
            segment //= section.length()

    def addToSequence(self, part):
        if self.seq:
            part.prev = self.seq[-1]
        self.seq.append(part)

    def __iter__(self):
        allSequences = product(*self.seq)
        for exprList in allSequences:
            expPart, strPart = zip(*exprList)
            expression = ''.join(expPart)
            rep = ''.join(strPart)
            if self.hasValidParens(expression):
                yield expression, rep

    # What's faster, validating parens or catching an exception?
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
