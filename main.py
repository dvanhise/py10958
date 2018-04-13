from Sequence import Sequence
from Logger import Logger
from tqdm import tqdm

import sys
import re

from evaluator import eval_expr
from settings import *

l = Logger()


def main():
    if len(sys.argv) < 2:
        invalidArgs()

    action = sys.argv[1]
    if action == 'run':
        run(int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 0)
    elif action == 'result':
        getResult(int(sys.argv[2]))
    elif action == 'results':
        l.outputToFile(MAX_NUMBER)
    else:
        invalidArgs()


def invalidArgs():
    print("Run a segment:      main.py run <segment #> [<sub-segment #>]")
    print("Get one result:     main.py result <number>")
    print("Generate results:   main.py results")
    sys.exit(1)


def run(segmentNum, subSegmentNum=0):
    seq = Sequence(DIGIT_SEQUENCE, segmentNum, subSegmentNum)
    for expression in tqdm(seq):
        result = eval_expr(expression)

        if result and 0 < result <= MAX_NUMBER and float(result).is_integer():
            result = int(result)
            rep = getPrettyVersion(expression)
            l.log(rep, result)


def getPrettyVersion(expr):
    expr = expr.replace('**', '^')
    expr = re.sub(r'%s(?P<num>[0-9]+)' % C_SQRT, lambda m: '√' + m.group('num'), expr)
    expr = re.sub(r'%s(?P<num>[0-9]+)' % C_FACT, lambda m: m.group('num') + '!', expr)
    return expr


def getResult(number):
    print(l.getById(number))


if __name__ == "__main__":
    main()
