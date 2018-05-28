import multiprocessing as mp
from itertools import zip_longest
from tqdm import tqdm

from settings import *
from logger import Logger

import re


class Runner:

    def __init__(self, gen, evaluator):
        self.gen = gen
        self.evaluator = evaluator

        self.logger = Logger()

    def run(self):
        def grouper(iterable, n):
            args = [iter(iterable)] * n
            return zip_longest(*args)

        batch_last = results_last = pool_last = None
        for batch in grouper(tqdm(self.gen), BATCH_SIZE):

            if batch_last:
                to_add = []
                # Block until we get the results of the last batch
                results = results_last.get()
                pool_last.close()
                for result, expr in zip(results, batch_last):
                    if result and 0 < result <= MAX_NUMBER and float(result).is_integer():
                        to_add.append((int(result), self.getPrettyVersion(expr)))

            pool_last = mp.Pool(processes=NUM_COMPUTE_PROCESSES)
            results_last = pool_last.map_async(self.evaluator, batch, 1000)

            if batch_last:
                self.logger.addManyToDb(to_add)
            batch_last = batch

    def getPrettyVersion(self, expr):
        expr = expr.replace('**', '^')
        expr = re.sub(r'%s(?P<num>[0-9]+)' % C_SQRT, lambda m: '√' + m.group('num'), expr)
        expr = re.sub(r'%s(?P<num>[0-9]+)' % C_FACT, lambda m: m.group('num') + '!', expr)
        return expr
