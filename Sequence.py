from Part import Part
from itertools import product


class Sequence(object):

    seq = []

    def __init__(self, digitList):
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

    def nextParenSet(self):
        # TODO: paren stuff
        yield

    def __iter__(self):
        # for a in self.nextParenSet():
        i = product(*self.seq)
        for x in i:
            yield ''.join(x)
