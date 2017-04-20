from Part import Part


class Sequence(object):

    seq = []

    def __init__(self, digitList):
        for ndx, val in enumerate(digitList):
            if ndx > 0:
                self.seq.append(Part('op'))

            if ndx < len(digitList) - 1:
                self.seq.append(Part('pre'))

            self.seq.append(Part('dig', val))

            if ndx > 1:
                self.seq.append(Part('post'))

    def evaluate(self):
        return eval(self.toString())

    def toString(self):
        str = ''
        for part in self.seq:
            str += part.toString()
        return str