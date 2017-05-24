class Part:

    # options should be list of (<part of expression>, <print representation>) tuples
    options = []
    freeze = None

    def lock(self, ndx, prev):
        if self.options[ndx] in self.filterOptions(prev):
            self.freeze = self.options[ndx]
            return self.freeze
        else:
            # If a locked part is invalid, the entire test segment is invalid
            raise ValueError

    def unlock(self):
        self.freeze = None

    def length(self):
        return len(self.options)

    def getIterator(self, prev):
        if self.freeze is not None:
            return [self.freeze]
        else:
            return self.filterOptions(prev)

    def filterOptions(self, prev):
        return self.options
