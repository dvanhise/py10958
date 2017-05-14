from Sequence import Sequence
from Logger import Logger
from tqdm import tqdm
import sys
from evaluator import eval_expr

DIGIT_SEQUENCE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
STATIC_PARTS = 8  # Determines how many segments the problem is broken into, higher number means more pieces
MAGIC_NUMBER = 10958
MAX_NUMBER = 100000

EVAL_TIMEOUT = 1
LOG_FREQUENCY = 600

l = Logger()


def main():
    if len(sys.argv) < 2:
        invalidArgs()

    if sys.argv[1] == 'run':
        run(int(sys.argv[2]))
    elif sys.argv[1] == 'result':
        getResult(int(sys.argv[2]))
    elif sys.argv[1] == 'results':
        l.outputToFile(MAX_NUMBER)
        sys.exit()
    else:
        invalidArgs()


def invalidArgs():
    print("Usage: main.py run <segment #>")
    print("or     main.py result <number>")
    print("or     main.py results")
    sys.exit(1)


def run(segmentNum):
    seq = Sequence(DIGIT_SEQUENCE, STATIC_PARTS, segmentNum)

    l.logText('Running segment %d' % segmentNum)
    for expression, rep in tqdm(seq):
        try:
            result = eval_expr(expression)
            if (type(result) is float and result.is_integer()) or type(result) is int:
                result = int(result)

                if 0 < result < MAX_NUMBER:
                    l.log(rep, result)
                if result == MAGIC_NUMBER:
                    l.logText('Result: %d, Sequence: %s' % (result, rep))
        # possible errors from evaluating the expression
        except (ValueError, SyntaxError, ZeroDivisionError, OverflowError):
            pass
    l.logText('Segment %d complete, results saved' % segmentNum)


def getResult(number):
    print(l.getById(number))


if __name__ == "__main__":
    main()
