from part.neg import Neg
from part.op import Op
from part.pre import Pre
from part.post import Post
from part.number import Number
from part.unary import Unary
from functools import reduce
from settings import C_CONCAT, C_FACT, C_SQRT
import re


class Sequence:
    seq = []
    staticPart = ''

    def __init__(self, digitList, staticParts=0, segment=0):
        for ndx, val in enumerate(digitList):
            if ndx == 0:
                self.addToSequence(Neg())
            if ndx > 0:
                self.addToSequence(Op())

            if ndx < len(digitList) - 1:
                self.addToSequence(Pre())
            self.addToSequence(Unary())
            self.addToSequence(Number(val))
            if ndx > 0:
                self.addToSequence(Post())

        staticSection = self.seq[:staticParts]
        segments = reduce(lambda x, y: x * y.length(), staticSection, 1)
        print('Test set broken into %d segments' % segments)

        if segment >= segments:
            print('Segment number out of bounds')
            raise IndexError

        for section in staticSection:
            v = segment % section.length()
            self.staticPart += section.lock(v, self.staticPart)
            segment //= section.length()

    def addToSequence(self, part):
        self.seq.append(part)

    def __iter__(self):
        for expression in self.forParts(self.seq):
            if self.hasValidParens(expression):
                yield expression

    # This is my implementation of itertools.product that allows each part to base the options
    # it returns off of any earlier part of the generated sequence and doesn't use all memory
    def forParts(self, parts, expr=''):
        if parts:
            options = parts[0].getIterator(expr)
            for opt in options:
                for a in self.forParts(parts[1:], expr + opt):
                    yield a
        else:
            yield expr

    def getPrettyVersion(self, expr):
        expr = expr.replace(C_CONCAT, '').replace('**', '^')
        expr = re.sub(r'%s(?P<num>[0-9]+)' % C_SQRT, lambda m: '√' + m.group('num'), expr)
        expr = re.sub(r'%s(?P<num>[0-9]+)' % C_FACT, lambda m: m.group('num') + '!', expr)
        return expr

    def hasValidParens(self, exp):
        unmatched = 0
        for char in exp:
            if char == '(':
                unmatched += 1
            elif char == ')':
                if unmatched == 0:
                    return False
                unmatched -= 1
        return unmatched == 0

    def getStaticParts(self):
        return ''.join(self.staticPart)
