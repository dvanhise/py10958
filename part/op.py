from part.part import Part


class Op(Part):

    options = [('+', '+'),
               ('-', '-'),
               ('*', '*'),
               ('/', '/'),
               ('**', '^'),
               ('', '')]

    def isValid(self):
        if not self.current:
            post = self.getPrev('Post')
            if post and post.current:
                return False
            num = self.getPrev('Number')
            if num and num.isChanged():
                return False
        return True
