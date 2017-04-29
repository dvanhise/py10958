from Sequence import Sequence
from Logger import Logger
from WinTimeoutDecorator import timeout
from tqdm import tqdm
import sys

DIGIT_SEQUENCE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
STATIC_PARTS = 5
MAGIC_NUMBER = 10958
MAX_NUMBER = 20000

EVAL_TIMEOUT = 1
LOG_FREQUENCY = 600

l = Logger()


def main():
    if len(sys.argv) != 3:
        invalidArgs()

    if sys.argv[1] == 'run':
        run(int(sys.argv[2]))
    elif sys.argv[1] == 'result':
        getResult(int(sys.argv[2]))
    else:
        invalidArgs()


def invalidArgs():
    print("Usage: 10958.py run <segment #>")
    print("or     10958.py result <number>")
    sys.exit(1)


def run(segmentNum):
    seq = Sequence(DIGIT_SEQUENCE, STATIC_PARTS, segmentNum)

    l.logText('Running segment %d' % segmentNum)
    for expression in tqdm(seq):
        try:
            result = evalWrapper(expression)
            if (type(result) is float and result.is_integer()) or type(result) is int:
                result = int(result)

                if 0 < result < MAX_NUMBER:
                    l.log(expression, result)
                if result == MAGIC_NUMBER:
                    print('Result: %d, Sequence: %s' % (result, expression))
        except TimeoutError:
            l.logSkipped(expression)
        except (ValueError, SyntaxError, ZeroDivisionError, OverflowError):
            pass
        except:
            print("Unexpected error %s with sequence %s" % (sys.exc_info()[0], expression))
    l.logText('Segment %d complete, results saved' % segmentNum)


def getResult(number):
    print(l.getById(number))


# @timeout(EVAL_TIMEOUT)
def evalWrapper(exp):
    return eval(exp)

if __name__ == "__main__":
    main()
