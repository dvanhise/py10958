from part.part import Part


class Post(Part):
    options = [('', ''), (')', ')')]

    def isValid(self):
        if self.current:
            # This checks for redundant parentheses
            pre = self.getPrev('Pre', maxSteps=2)
            if pre and pre.current:
                return False
        return True
