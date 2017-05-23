from part.part import Part
from settings import C_CONCAT


class Pre(Part):
    options = ['', '(']

    def filterOptions(self, prev):
        # This prevents an open paren being right after a concatenate operation
        return self.options if prev and prev[-1] != C_CONCAT else [o for o in self.options if not o]
