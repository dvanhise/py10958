from part.part import Part


class Post(Part):
    options = ['', ')']

    def isValid(self):
        if self.current:
            # This checks for redundant parentheses
            pre = self.prev.prev
            if pre.getType() == 'Pre' and pre.current:
                return False
        return True
