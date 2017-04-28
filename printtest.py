import threading

a = 0.0


def printCurrentResults():
    print(a)
    threading.Timer(1, printCurrentResults).start()

printCurrentResults()

while 1:
    a += .00000001
    if a > 10000000000:
        a = 0
