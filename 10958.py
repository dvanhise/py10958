from Sequence import Sequence
from timeout_decorator import TimeoutError, timeout

DIGIT_SEQUENCE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
MAGIC_NUMBER = 10958
EVAL_TIMEOUT = 2


def main():
    logDict = {
        'int': 0,
        'float': 0,
        'timeout': 0,
        'other': 0
    }

    seq = Sequence(DIGIT_SEQUENCE)
    for expression in seq:
        try:
            result = evalWrapper(expression)
            if (type(result) is float and result.is_integer()) or type(result) is int:
                result = int(result)
                if (result > 10 and result < 50) or result == MAGIC_NUMBER:
                    print('Result: {}, Sequence: {}'.format(result, expression))
                logDict['int'] += 1
            else:
                logDict['float'] += 1
        except TimeoutError:
            logDict['timeout'] += 1
        except:
            logDict['other'] += 1

        print(logDict)


@timeout(EVAL_TIMEOUT, timeout_exception=TimeoutError)
def evalWrapper(exp):
    return eval(exp)

if __name__ == "__main__":
    main()
