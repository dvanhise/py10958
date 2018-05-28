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

        self.cache = self.getAsDict()

    @db_session
    def getAsDict(self):
        return dict(select((r.value, r.expression) for r in Result))

    def saveResult(self, result, rep):
        fetched = self.cache.get(result)
        if not fetched or len(rep) < len(fetched):
            self.cache[result] = rep
            self.addToDb(result, rep)

    # Pairs is a list of result, expression tuples
    @db_session
    def addManyToDb(self, pairs):
        for result, rep in pairs:
            fetched = self.cache.get(result)
            if not fetched:
                Result(value=result, expression=rep)
                self.cache[result] = rep
            elif len(rep) < len(fetched):
                entry = Result[result]
                entry.expression = rep
                self.cache[result] = rep

    @db_session
    def addToDb(self, result, expression):
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
            d = self.getAsDict()
            for i in range(1, upTo+1):
                exp = d.get(i)
                f.write('%5d = %s\n' % (i, exp))


class Result(db.Entity):
    value = PrimaryKey(int)
    expression = Required(str)
