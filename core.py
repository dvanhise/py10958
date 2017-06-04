import math
from settings import C_SQRT, C_FACT


class CoreFactory:
    last = False

    def __init__(self, num, last=False):
        self.num = num
        self.last = last

    def getUnaryOps(self):
        ops = ['', '-']
        num = int(self.num)
        if num > 1 and math.sqrt(num).is_integer():
            ops.append(C_SQRT)
        if 2 < num < 20:
            ops.append(C_FACT)
        return ops

    def __iter__(self):
        for uop in self.getUnaryOps():
            if self.last:
                yield Core(self.num, '', uop, last=True)
            else:
                for op in ['+', '-', '*', '/', '**']:
                    yield Core(self.num, op, uop)


class Core:

    preParen = False
    postParen = False
    unaryOp = ''
    op = ''
    last = False

    def __init__(self, num, op, uop, last=False):
        self.num = num
        self.op = op
        self.uop = uop
        self.last = last

    def setParen(self, paren):
        self.preParen = (paren == '(')
        self.postParen = (paren == ')')

    def setLast(self):
        self.last = True

    def getStr(self):
        return '{}{}{}{}{}'.format('(' if self.preParen else '',
                                   self.unaryOp,
                                   self.num,
                                   ')' if self.postParen else '',
                                   self.op if not self.last else '')
