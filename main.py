from Sequence import Sequence
from logger import Logger

import sys

from evaluator import eval_expr
from settings import *
from runner import Runner


def main():
    if len(sys.argv) < 2:
        invalidArgs()

    action = sys.argv[1]
    if action == 'run':
        run(int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 0)
    elif action == 'result':
        getResult(int(sys.argv[2]))
    elif action == 'results':
        Logger().outputToFile(MAX_NUMBER)
    else:
        invalidArgs()


def invalidArgs():
    print("Run a segment:      main.py run <segment #> [<sub-segment #>]")
    print("Get one result:     main.py result <number>")
    print("Generate results:   main.py results")
    sys.exit(1)


def run(segmentNum, subSegmentNum=0):
    seq = Sequence(DIGIT_SEQUENCE, segmentNum, subSegmentNum)
    r = Runner(seq, eval_expr)
    r.run()


def getResult(number):
    print(Logger().getById(number))


if __name__ == "__main__":
    main()
