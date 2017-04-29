
class Part(object):

    def __init__(self, options):
        self.options = options
        self.val = None

    def lock(self, ndx):
        self.val = self.options[ndx]

    def unlock(self):
        self.val = None

    def length(self):
        return len(self.options)

    def __iter__(self):
        if self.val:
            yield str(self.val)
        else:
            for rep in self.options:
                yield rep
