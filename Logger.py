from pony.orm import *


db = Database()

DB_NAME = '10958.sqlite.db'
LOG_FILE = 'log.txt'
SKIPPED_FILE = 'skipped.txt'


class Logger(object):

    def __init__(self):
        # Create database and tables if they don't exist
        db.bind('sqlite', DB_NAME, create_db=True)
        db.generate_mapping(create_tables=True)

        self.cache = {}

    @db_session
    def log(self, expression, result):
        # Don't touch the database if we've saved a shorter expression with the same result
        fetched = self.cache.get(str(result))
        if fetched and len(expression) >= fetched:
            return

        try:
            entry = Result[result]
            if len(expression) < len(entry.expression):
                entry.expression += expression
                self.cache[str(result)] = len(expression)
            else:
                self.cache[str(result)] = len(entry.expression)
        except core.ObjectNotFound:
            Result(value=result, expression=expression)

    @db_session
    def getById(self, id):
        try:
            return Result[id].expression
        except core.ObjectNotFound:
            return None

    def logText(self, text):
        with open(LOG_FILE, 'a') as f:
            f.write(text + '\n')

    def logSkipped(self, exp):
        with open(SKIPPED_FILE, 'a') as f:
            f.write(exp + '\n')


class Result(db.Entity):
    value = PrimaryKey(int)
    expression = Required(str)
