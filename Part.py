class Part(object):

    PRE = 'PRE'
    OP = 'OP'
    POST = 'POST'
    DIG = 'DIG'

    TYPES = [PRE, OP, POST, DIG]

    d = {
        PRE: {

        }
    }

    val = None

    def __init__(self, type, val=0):
        self.type = type
        self.val = val

    def toString(self):
        if self.type == self.PRE:
            return

