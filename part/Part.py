class Part:

    # options should be list of (<part of expression>, <print representation>) tuples
    options = []
    freeze = None
    prev = None
    current = None

    def lock(self, ndx):
        self.freeze = self.options[ndx]
        self.current = self.freeze[0]

    def unlock(self):
        self.freeze = None

    def length(self):
        return len(self.options)

    def __iter__(self):
        if self.freeze is not None:
            if self.isValid():
                yield self.freeze
        else:
            for exp, rep in self.options:
                temp = self.current
                self.current = exp
                if self.isValid():
                    yield (exp, rep)
                else:
                    self.current = temp

    def getType(self):
        return type(self).__name__

    def isValid(self):
        return True

    def getPrev(self, partType, maxSteps=None):
        here = self.prev
        iterations = 1
        while 1:
            if not here:
                return None
            elif here.getType() == partType:
                return here
            elif maxSteps and iterations >= maxSteps:
                return None
            here = here.prev
            iterations += 1
