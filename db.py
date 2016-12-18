import sqlite3


class DbConnection:
    def __init__(self):
        self.conn = None

    def connect(self, db_file):
        self.conn = sqlite3.connect(db_file)

    def execute(self, query):
        self.conn.execute(query)

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    dbc = DbConnection()
    dbc.connect("./saves/game01.db")
    dbc.close()
