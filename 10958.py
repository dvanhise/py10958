from Sequence import Sequence
from timeout_decorator import TimeoutError, timeout

DIGIT_SEQUENCE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
MAGIC_NUMBER = 10958
EVAL_TIMEOUT = 2


def main():
    seq = Sequence(DIGIT_SEQUENCE)
    for expression in seq:
        try:
            result = evalWrapper(expression)
            if type(result) is float and result.is_integer():
                result = int(result)
            if result == MAGIC_NUMBER:
                print('Result: {d}, Sequence: {s}'.format(result, expression))
        except TimeoutError:
            print('Timeout: ' + expression)
        except:
            print('Other failure: ' + expression)
            raise


@timeout(EVAL_TIMEOUT, timeout_exception=StopIteration)
def evalWrapper(exp):
    return eval(exp)

if __name__ == "__main__":
    main()
