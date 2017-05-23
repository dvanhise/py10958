from part.part import Part


class Post(Part):
    options = ['', ')']

    def filterOptions(self, prev):
        if prev.count('(') <= prev.count(')'):
            return [o for o in self.options if not o]

        # Check for redundant parentheses
        for char in reversed(prev):
            if char in '+-/*':
                return self.options
            elif char == '(':
                break
        return [o for o in self.options if not o]
