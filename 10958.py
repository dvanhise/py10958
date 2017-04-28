from Sequence import Sequence
from WinTimeoutDecorator import timeout
from tqdm import tqdm
import threading

DIGIT_SEQUENCE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
MAGIC_NUMBER = 10958

EVAL_TIMEOUT = 1
LOG_FREQUENCY = 600


def main():
    logDict = {
        'int': 0,
        'float': 0,
        'timeout': 0,
        'other': 0
    }
    resultDict = {}

    def printCurrentResults():
        print(logDict)
        print(resultDict)
        print('\n' + '-'*50 + '\n')
        threading.Timer(LOG_FREQUENCY, printCurrentResults).start()

    printCurrentResults()
    seq = Sequence(DIGIT_SEQUENCE)
    for expression in tqdm(seq):
        try:
            result = evalWrapper(expression)
            if (type(result) is float and result.is_integer()) or type(result) is int:
                result = int(result)
                if result == MAGIC_NUMBER:
                    print('Result: {}, Sequence: {}'.format(result, expression))

                strResult = str(result)
                if strResult in resultDict:
                    resultDict[strResult] += [expression]
                else:
                    resultDict[strResult] = [expression]
                logDict['int'] += 1
            else:
                logDict['float'] += 1
        except TimeoutError:
            logDict['timeout'] += 1
        except:
            logDict['other'] += 1


@timeout(EVAL_TIMEOUT)
def evalWrapper(exp):
    return eval(exp)

if __name__ == "__main__":
    main()
