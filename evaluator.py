'''
Source: stackoverflow.com/questions/2371436/evaluating-a-mathematical-expression-in-a-string/9558001#9558001
'''
import ast
import operator as op


def eval_expr(expr):
    return eval_(ast.parse(expr, mode='eval').body)


def eval_(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)


def power(a, b):
    if abs(a*b) > 10**5:
        raise ValueError((a, b))
    return op.pow(a, b)


# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: power, ast.BitXor: op.xor,
             ast.USub: op.neg}
