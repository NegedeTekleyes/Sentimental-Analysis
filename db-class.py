import sys
class Database:
    def __init__(self, name):
        self.name = name
        self.tables = {}

    def add_tables(self):
        table_name = input("Enter the table name: ")
        self.tables[table_name] = {}
        return table_name

    def add_columns(self, table_name):
        self.tables[table_name]['columns'] = []
        number_of_cols = int(input("Enter the number of columns: "))

        for i in range(number_of_cols):
            col = input(f"Enter column name {i+1}: ")
            self.tables[table_name]['columns'].append(input(f'Enter the column name'))

    def __str__(self):
        return f"Database: {self.name}\nTables: {self.tables}"


class App:
    @staticmethod
    def main():
        if len(sys.argv) < 2:
            print("Usage: python db-class.py create_db LMS")
            return

        if sys.argv[1] == 'create_db':
            db = Database(sys.argv[2])
            table_name = db.add_tables()
            db.add_columns(table_name)
            print(db)
        else:
            print("Invalid command")


if __name__ == "__main__":
    App.main()
