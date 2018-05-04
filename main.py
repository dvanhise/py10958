from Sequence import Sequence
from Logger import Logger
from tqdm import tqdm

import multiprocessing as mp
from itertools import zip_longest
import sys
import re

from evaluator import eval_expr, eval_batch
from settings import *


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
    pool = mp.Pool(processes=NUM_PROCESSES, maxtasksperchild=10)
    manager = mp.Manager()
    queue = manager.Queue()

    for batch in grouper(tqdm(seq), BATCH_SIZE):
        pool.apply_async(eval_batch, (batch, queue,))

        for i in range(queue.qsize()//3):
            consume(queue)

    # Finish and consume all jobs in progress
    pool.close()
    pool.join()
    while not queue.empty():
        consume(queue)


def consume(queue):
    batch = queue.get()
    for expression, result in batch:
        if result and 0 < result <= MAX_NUMBER and float(result).is_integer():
            result = int(result)
            rep = getPrettyVersion(expression)
            Logger().log(rep, result)


def grouper(iterable, n):
    # grouper('ABCDEFG', 3) --> ABC DEF G"
    args = [iter(iterable)] * n
    return zip_longest(*args)


def getPrettyVersion(expr):
    expr = expr.replace('**', '^')
    expr = re.sub(r'%s(?P<num>[0-9]+)' % C_SQRT, lambda m: '√' + m.group('num'), expr)
    expr = re.sub(r'%s(?P<num>[0-9]+)' % C_FACT, lambda m: m.group('num') + '!', expr)
    return expr


def getResult(number):
    print(Logger().getById(number))


if __name__ == "__main__":
    main()
