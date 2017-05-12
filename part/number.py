from part.part import Part
import math


class Number(Part):

    def __init__(self, val):
        super(Number).__init__()
        self.initVal = str(val)
        self.options = [str(val), str(math.factorial(val))]
        if math.sqrt(val).is_integer():
            self.options.append(str(int(math.sqrt(val))))

    def isValid(self):
        if self.current != self.initVal:
            op = self.prev.prev
            if op and op.getType() == 'Op' and not op.current:
                return False
        return True


# Is using square root cheating within the rules of the problem?
# Adding an arbitrary ^2 would not be allowed unless that was the two
# in the number set, so ^(1/2) seems even more wrong.  It's only
# redeeming factor is that the written form of square root only
# consists of a symbol (√), making it more similar to factorial (!).

# Since the problem itself isn't too mathematically serious, I'm keeping it.
