from part.part import Part


class Op(Part):

    options = ['+', '-', '*', '/', '**', '']

    def isValid(self):
        # This checks for a possible invalid condition when there's no operation
        if not self.current:
            pre = self.prev
            if pre.getType() == 'Pre' and pre.current:
                return False
        return True
