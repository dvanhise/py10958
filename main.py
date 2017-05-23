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
        run(int(sys.argv[2]))
    elif action == 'result':
        getResult(int(sys.argv[2]))
    elif action == 'results':
        l.outputToFile(MAX_NUMBER)
    else:
        invalidArgs()


def invalidArgs():
    print("Run a segment:      main.py run <segment #>")
    print("Get one result:     main.py result <number>")
    print("Generate results:   main.py results")
    sys.exit(1)


def createSequence(segmentNum):
    try:
        return Sequence(DIGIT_SEQUENCE, STATIC_PARTS, segmentNum)
    except ValueError:
        l.logText('Segment %d invalid' % segmentNum)
        print('All possible expressions from this segment are invalid.')
        sys.exit(0)


def run(segmentNum):
    seq = createSequence(segmentNum)
    print("Static part: '%s'" % seq.getStaticParts())
    l.logText('Running segment %d' % segmentNum)
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
    l.logText('Segment %d complete' % segmentNum)


def getResult(number):
    print(l.getById(number))


if __name__ == "__main__":
    main()
