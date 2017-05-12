from Logger import *

MAX_NUMBER = 20000

db = Database()
l = Logger()

missing = []

with open('output.txt', 'a') as f:
    for i in range(1, MAX_NUMBER+1):
        exp = l.getById(i)
        if not exp:
            missing.append(i)
        print('%5d - %s' % (i, exp))
