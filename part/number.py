from part.part import Part


class Number(Part):

    def __init__(self, val):
        super(Number).__init__()
        self.options = [str(val)]
