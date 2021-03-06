from core import CoreFactory
from itertools import product
from settings import C_FACT, C_SQRT


SUB_SEG_GRANULARITY = 10**5


class Sequence:
    seq = []
    staticPart = ''

    def __init__(self, digitList, segmentNum, subSegmentNum=0):
        self.digitList = [str(d) for d in digitList]
        self.segmentNum = segmentNum
        self.subSegmentNum = subSegmentNum * SUB_SEG_GRANULARITY
        self.parenSetCache = {}

    # Generate every possible mathematical expression using digitList digits in order
    def __iter__(self):
        for numList in self.iterConcatenation(self.digitList):
            cores = [CoreFactory(num, ndx == 0) for ndx, num in enumerate(numList)]
            for coreList in self.iterBaseCores(cores):
                for finalCoreList in self.iterParens(coreList):
                    exp = ''.join([core.getStr() for core in finalCoreList])
                    yield exp

    def hasValidParens(self, parenList):
        unmatched = 0
        for char in parenList:
            if char == '(':
                unmatched += 1
            elif char == ')':
                if unmatched == 0:
                    return False
                unmatched -= 1
        return unmatched == 0

    def getValidParenSets(self, length):
        if length in self.parenSetCache:
            return self.parenSetCache[length]

        self.parenSetCache[length] = []
        for parenSet in product([None, '(', ')'], repeat=length):
            if self.hasValidParens(parenSet):
                self.parenSetCache[length].append(parenSet)
        return self.parenSetCache[length]

    # Generate all possible ways to concatenate or not the indices of numberList
    def iterConcatenation(self, numberList):
        # Generate all possible lists of True/False of length n-1, join the indices in that way
        length = len(numberList) - 1
        for segment, concat in enumerate(product([False, True], repeat=length)):
            if segment >= self.segmentNum:
                # Copy the list and create a unique concatenation of it
                subList = numberList[:]
                for ndx, c in enumerate(concat, start=1):
                    if c:
                        # Must be done in reverse
                        i = len(concat) - ndx
                        subList[i:i+2] = [''.join(subList[i:i+2])]
                print('Segment %d started: %s' % (segment, ' '.join(subList)))
                yield subList
                print('Segment %d complete: %s' % (segment, ' '.join(subList)))

    # Generate all possible combinations of core attributes (operation, unary op) for each core
    def iterBaseCores(self, cores):
        for segment, seq in enumerate(product(*cores)):
            if segment > self.subSegmentNum:
                yield seq
                if segment % SUB_SEG_GRANULARITY == 0:
                    print('Sub-segment %d complete' % (segment/SUB_SEG_GRANULARITY - 1))
        self.subSegmentNum = 0   # Start at subsegment 0 for all future segments

    # Generate all possible ways to validly parenthesize the list of cores
    def iterParens(self, cores):
        for parenSet in self.getValidParenSets(len(cores)):
            for i, paren in enumerate(parenSet):
                cores[i].setParen(paren)
            yield cores
