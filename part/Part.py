class Part:

    options = []
    freeze = None
    prev = None
    current = None

    def lock(self, ndx):
        self.freeze = self.options[ndx]

    def unlock(self):
        self.freeze = None

    def length(self):
        return len(self.options)

    def __iter__(self):
        if self.freeze is not None:
            yield str(self.freeze)
        else:
            for rep in self.options:
                self.current = rep
                if self.isValid():
                    yield rep

    def getType(self):
        return type(self).__name__

    def isValid(self):
        return True
