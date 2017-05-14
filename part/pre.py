from part.part import Part


class Pre(Part):
    options = [('', ''), ('(', '(')]

    def isValid(self):
        # This checks for a possible invalid condition when there's no operation
        if self.current:
            op = self.getPrev('Op')
            if op and not op.current:
                return False
        return True

