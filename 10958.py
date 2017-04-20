from Sequence import Sequence
from timeout_decorator import TimeoutError, timeout

DIGIT_SEQUENCE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
MAGIC_NUMBER = 10958


def main():
    seq = Sequence(DIGIT_SEQUENCE)
    for expression in seq:
        # print('test: ' + expression)
        try:
            result = evalWrapper(expression)
            if type(result) is int and abs(result - MAGIC_NUMBER) < 5:
                print('Result: {d}, Sequence: {s}'.format(result, expression))
        except TimeoutError:
            print('Timeout: ' + expression)
        except:
            print('Other failure: ' + expression)
            raise


@timeout(2, timeout_exception=StopIteration)
def evalWrapper(exp):
    return eval(exp)

if __name__ == "__main__":
    main()
