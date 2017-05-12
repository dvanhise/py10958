from Logger import *

MAX_NUMBER = 11111

db = Database()
l = Logger()

missing = []

for i in range(1, MAX_NUMBER+1):
    exp = l.getById(i)
    if not exp:
        missing.append(i)
    print('%5d - %s' % (i, exp))

print('Missing: ' + ', '.join([str(x) for x in missing]))
print('Total: %d' % len(missing))
