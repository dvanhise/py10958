from part.part import Part
import math


class Number(Part):

    def __init__(self, val):
        super(Number).__init__()
        v = str(val)
        self.initVal = v
        self.options = [(v, v), (str(math.factorial(val)), v+'!')]
        if math.sqrt(val).is_integer():
            self.options.append(
                (str(int(math.sqrt(val))), '√'+v))

    def isValid(self):
        # Prevents digit concatenation when factorial or square root was applied to either
        op = self.getPrev('Op')
        if op and not op.current and self.isChanged():
            return False
        return True

    def isChanged(self):
        return self.current != self.initVal

# Is using square root cheating within the rules of the problem?
# Adding an arbitrary ^2 would not be allowed unless that was the two
# in the number set, so ^(1/2) seems even more wrong.  It's only
# redeeming factor is that the written form of square root only
# consists of a symbol (√), making it more similar to factorial (!).

# Since the problem itself isn't too mathematically serious, I'm keeping it.
