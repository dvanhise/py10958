from Part import Part
from itertools import product
from functools import reduce
import re


PRE = ['', '(']
# OP = ['+', '-', '*', '/', '**', '']
OP = ['+', '-', '*', '/', '']
POST = ['', ')']
NEG = ['', '-']

redundantParensRe = re.compile(r'\([0-9]+\)')
isMathRe = re.compile(r'[0-9]+[()]{1,2}[0-9]+')


class Sequence(object):

    seq = []

    def __init__(self, digitList, staticParts=0, segment=0):
        # str = -(1)+(2)+(3)...
        for ndx, val in enumerate(digitList):
            if ndx == 0:
                self.seq.append(Part(NEG))

            if ndx > 0:
                self.seq.append(Part(OP))

            if ndx < len(digitList) - 1:
                self.seq.append(Part(PRE))

            self.seq.append(Part([str(val)]))

            if ndx > 1:
                self.seq.append(Part(POST))

        staticSection = self.seq[:staticParts]
        segments = reduce(lambda x, y: x * y.length(), staticSection, 1)
        print('Sequence broken into %d segments' % segments)

        if segment >= segments:
            print('Segment number out of bounds')
            raise IndexError

        for section in staticSection:
            v = segment % section.length()
            section.lock(v)
            segment //= section.length()

    def __iter__(self):
        allSequences = product(*self.seq)
        for x in allSequences:
            expression = ''.join(x)
            if self.isValid(expression):
                yield expression

    def isValid(self, exp):
        return self.hasValidParens(exp) and \
               not self.hasRedundantParens(exp) and \
               self.isMath(exp) and \
               not self.isTooMathy(exp)

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

    def hasRedundantParens(self, exp):
        return redundantParensRe.search(exp)

    def isMath(self, exp):
        return not isMathRe.search(exp)

    def isTooMathy(self, exp):
        return exp.count('**') >= 2
