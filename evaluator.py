'''
Source: stackoverflow.com/questions/2371436/evaluating-a-mathematical-expression-in-a-string/9558001#9558001
'''
import ast
import operator as op
import re
import math
from settings import C_FACT, C_SQRT


def eval_expr(expr):
    return eval_(ast.parse(preeval(expr), mode='eval').body)


def eval_(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)


def preeval(expr):
    expr = re.sub(r'%s(?P<num>[0-9]+)' % C_SQRT, lambda m: sqrt(int(m.group('num'))), expr)
    expr = re.sub(r'%s(?P<num>[0-9]+)' % C_FACT, lambda m: factorial(int(m.group('num'))), expr)
    return expr


# Very high power calculations may not finish calculating this year (e.g. try 9**9**9**9**9**9**9**9**9)
# Raising to a power far less than 0 results in an infinitesimal that gets rounded off
# No raising negative numbers to a non-integer power, complex results are not ok
def power(a, b):
    if abs(a*b) > 10**4 or b < -5 or (a < 0 and not float(b).is_integer()):
        raise ValueError
    return op.pow(a, b)


# Raise ValueError for very high denominators because the result might incorrectly be 0 (e.g. 1 + 1/(10**20) --> 1.0)
def truediv(a, b):
    if b > 10**10:
        raise ValueError
    return op.truediv(a, b)


def factorial(a):
    if a > 20:
        raise ValueError
    return str(math.factorial(a))


# If the result is irrational, raise ValueError
def sqrt(a):
    res = math.sqrt(a)
    if res.is_integer():
        return str(res)
    else:
        raise ValueError

# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: truediv, ast.Pow: power, ast.USub: op.neg}
