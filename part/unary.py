from part.part import Part
from settings import C_SQRT, C_FACT


class Unary(Part):

    options = ['', '-', C_SQRT, C_FACT]

    def filterOptions(self, prev):
        # Operators only allowed if after open paren or op, no '-' after op
        if prev:
            if prev[-1] in '+-*/':
                return [o for o in self.options if o != '-']
            elif prev[-1] != '(':
                return [o for o in self.options if not o]
        return self.options

# Is using square root cheating within the rules of the problem?
# Adding an arbitrary ^2 would not be allowed unless that was the two
# in the number set, so ^(1/2) seems even more wrong.  It's only
# redeeming factor is that the written form of square root only
# consists of a symbol (√), making it more similar to factorial (!).

# Since the problem itself isn't too mathematically serious, I'm keeping it.
