
class Part(object):

    PRE = 'PRE'
    OP = 'OP'
    POST = 'POST'
    DIG = 'DIG'
    NEG = 'NEG'

    TYPES = [PRE, OP, POST, DIG, NEG]

    repDict = {
        PRE: ['', '('],
        OP: ['+', '-', '*', '/', ''],
        POST: ['', ')'],
        NEG: ['', '-']
    }

    def __init__(self, type, val=None):
        print('New part: ' + type)
        self.type = type
        self.val = val

    def getType(self):
        return self.type

    def __iter__(self):
        if self.getType() == self.DIG:
            yield str(self.val)
        elif self.getType() in [self.PRE, self.POST]:
            yield ''
        else:
            for rep in self.repDict[self.getType()]:
                yield rep




'''
>>> 4**4
256
>>> 1+2-3*4/5**67
3.0
>>> 1+2-3*4/5*6
-11.399999999999999
>>> 1+2-3*45+6
-126
>>> a = [[2,4,8],[3,9,27],[4,16,64]]
>>> a
[[2, 4, 8], [3, 9, 27], [4, 16, 64]]
>>> import itertools
>>> itertools.chain.from_iterable(a)
<itertools.chain object at 0x000002270A122A20>
>>> b = itertools.chain.from_iterable(a)
>>> len(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'itertools.chain' has no len()
>>> b
<itertools.chain object at 0x000002270A12B0B8>
>>> b.count()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'itertools.chain' object has no attribute 'count'
>>> b[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'itertools.chain' object is not subscriptable
>>> next(b)
2
>>> next(b)
4
>>> next(b)
8
>>> next(b)
3
>>> a = [2,3,5]*3
>>> a
[2, 3, 5, 2, 3, 5, 2, 3, 5]
>>> a = [[2,3,5]]*3
>>> a
[[2, 3, 5], [2, 3, 5], [2, 3, 5]]
>>> c = [1,2,3,4,5]
>>> itertools.permutation(c, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'itertools' has no attribute 'permutation'
>>> itertools.permutations(c, 2)
<itertools.permutations object at 0x000002270A124150>
>>> f = itertools.permutations(c, 2)
>>> next(f)
(1, 2)
>>> next(f)
(1, 3)
>>> next(f)
(1, 4)
>>> next(f)
(1, 5)
>>> next(f)
(2, 1)
>>> next(f)
(2, 3)
>>> next(f)
(2, 4)
>>> f = itertools.combinations(c, 5)
>>> sum(next(f))
15
>>> sum(next(f))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> f = itertools.combinations(c*5, 5)
>>> sum(next(f))
15
>>> sum(next(f))
11
>>> sum(next(f))
12
>>> sum(next(f))
13
>>> sum(next(f))
14
>>> sum(next(f))
15
>>> [1,2,3]+[1]
[1, 2, 3, 1]
>>> f = itertools.combinations((c+[0])*5, 5)
>>> sum(next(f))
15
>>> sum(next(f))
10
>>> sum(next(f))
11
>>> sum(next(f))
12
>>> sum(next(f))
13
>>> sum(next(f))
14
>>> sum(next(f))
15
>>> sum(next(f))
10
>>> sum(next(f))
11
>>> sum(next(f))
12
>>> sum(next(f))
13
>>> sum(next(f))
14
>>> f = itertools.combinations(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Required argument 'r' (pos 2) not found
>>> a
[[2, 3, 5], [2, 3, 5], [2, 3, 5]]
>>> itertools.product(c)
<itertools.product object at 0x000002270A12A360>
>>> dd = itertools.product(c)
>>> next(dd)
(1,)
>>> next(dd)
(2,)
>>> next(dd)
(3,)
>>> next(dd)
(4,)
>>> next(dd)
(5,)
>>> dd = itertools.product(a)
>>> next(dd)
([2, 3, 5],)
>>> next(dd)
([2, 3, 5],)
>>> next(dd)
([2, 3, 5],)
>>> next(dd)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> asdf= [2,3,5]
>>> d = itertools.product(asdf, repeat=3)
>>> next(d)
(2, 2, 2)
>>> next(d)
(2, 2, 3)
>>> next(d)
(2, 2, 5)
>>> from operator import mul
>>> reduce(mul, next(d), 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reduce' is not defined
>>> from functools import reduce
>>> reduce(mul, next(d), 1)
12
>>> reduce(mul, next(d), 1)
18
>>> reduce(mul, next(d), 1)
30
>>> reduce(mul, next(d), 1)
20
>>> reduce(mul, next(d), 1)
30
>>>
'''