from Sequence import Sequence
from Logger import Logger
from tqdm import tqdm
import sys
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
        try:
            result = eval_expr(expression)
            if float(result).is_integer():
                result = int(result)
                rep = seq.getPrettyVersion(expression)

                if 0 < result <= MAX_NUMBER:
                    l.log(rep, result)
                if result == MAGIC_NUMBER:
                    l.logText('Result: %d, Sequence: %s' % (result, rep))
        except (ValueError, SyntaxError, ZeroDivisionError, OverflowError):
            # Possible errors from evaluating bad expressions
            pass
        except:
            print(expression)
            raise


def getResult(number):
    print(l.getById(number))


if __name__ == "__main__":
    main()
