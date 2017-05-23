from part.part import Part
from settings import C_CONCAT


class Op(Part):

    options = ['+', '-', '*', '/', '**', C_CONCAT]

    def filterOptions(self, prev):
        return self.options if prev and prev[-1].isdigit() else [o for o in self.options if o != C_CONCAT]
