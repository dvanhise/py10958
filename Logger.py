from pony.orm import *
from time import gmtime, strftime


db = Database()

DB_NAME = '10958.sqlite.db'
LOG_FILE = 'log.txt'


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Logger(object):

    def __init__(self):
        # Create database and tables if they don't exist
        db.bind('sqlite', DB_NAME, create_db=True)
        db.generate_mapping(create_tables=True)

        # initialize cache dictionary from database
        self.cache = self.getAsDict()

    def log(self, expression, result):
        # Don't touch the database if we've saved a shorter expression with the same result
        fetched = self.cache.get(result)
        if fetched and len(expression) >= len(fetched):
            return

        self.addToDb(expression, result)
        self.cache[result] = expression

    @db_session
    def getAsDict(self):
        return dict(select((r.value, r.expression) for r in Result))

    @db_session
    def addToDb(self, expression, result):
        try:
            entry = Result[result]
            entry.expression = expression
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
            f.write('[%s] %s\n' % (strftime("%H:%M:%S", gmtime()), text))

    def outputToFile(self, upTo):
        with open('output.txt', 'w', encoding="utf-8") as f:
            for i in range(1, upTo+1):
                exp = self.cache.get(i)
                f.write('%5d - %s\n' % (i, exp))


class Result(db.Entity):
    value = PrimaryKey(int)
    expression = Required(str)
