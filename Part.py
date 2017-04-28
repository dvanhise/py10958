
class Part(object):

    PRE = 'PRE'
    OP = 'OP'
    POST = 'POST'
    DIG = 'DIG'
    NEG = 'NEG'

    TYPES = [PRE, OP, POST, DIG, NEG]

    repDict = {
        PRE: ['', '('],
        OP: ['+', '-', '*', '/', '**', ''],
        POST: ['', ')'],
        NEG: ['', '-']
    }

    def __init__(self, type, val=None):
        self.type = type
        self.val = val

    def getType(self):
        return self.type

    def __iter__(self):
        if self.getType() == self.DIG:
            yield str(self.val)
        # elif self.getType() in [self.PRE, self.POST]:
        #     yield ''
        else:
            for rep in self.repDict[self.getType()]:
                yield rep
