import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            _is_done INTEGER DEFAULT 0,
            _is_deleted INTEGER DEFAULT 0,
            CreatedOn Data DEFAULT CURRENT_DATE,
            DueDate Date,
            UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """
        self.conn.execute(query)

    def create_user_table(self):
        query = """ 
        CREATE TABLE IF NOT EXISTS "User" (
        _id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Email TEXT, 
        CreatedOn Date default CURRENT_DATE
        );
        """
        self.conn.execute(query)

class ToDoModel:
    TABLENAME = "Todo"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def get_by_id(self, _id):
        where_clause = f"AND id={_id}"
        return self.list_items(where_clause)

    def create(self, text, description):
        query = f'insert into {self.TABLENAME} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}")'

        c = self.conn.cursor()
        #result = c.execute(query)
        #result = self.conn.commit()
        #self.conn.close()
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

    def select(self, text, description):
        query = f'values ("{text}","{description}")'

        result = self.conn.execute(query)
        return result

    def list_items(self, where_clause=""):
        query = f"SELECT id, Title, Description, DueDate, _is_done " \
                f"from {self.TABLENAME} WHERE _is_deleted != {1} " + where_clause
        print(query)
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result

    class User:
        TABLENAME = "User"

        def create(self, name, email):
            query = f'insert into {self.TABLENAME} ' \
                    f'(Name, Email) ' \
                    f'values ({name},{email})'
            result = self.conn.execute(query)
            return result