import math
from settings import C_SQRT, C_FACT


class CoreFactory:
    first = False

    def __init__(self, num, first=False):
        self.num = num
        self.first = first

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
            if self.first:
                yield Core(self.num, '', uop, first=True)
            # (x + -y) and (x - -y) are redundant forms of other shorter expressions and can be ignored
            elif uop == '-':
                for op in ['*', '/', '**']:
                    yield Core(self.num, op, uop)
            else:
                for op in ['+', '-', '*', '/', '**']:
                    yield Core(self.num, op, uop)


class Core:

    preParen = False
    postParen = False
    uop = ''
    op = ''
    first = False

    def __init__(self, num, op, uop, first=False):
        self.num = num
        self.op = op
        self.uop = uop
        self.first = first

    def setParen(self, paren):
        self.preParen = (paren == '(')
        self.postParen = (paren == ')')

    def getStr(self):
        return '{}{}{}{}{}'.format(self.op if not self.first else '',
                                   '(' if self.preParen else '',
                                   self.uop,
                                   self.num,
                                   ')' if self.postParen else '')
