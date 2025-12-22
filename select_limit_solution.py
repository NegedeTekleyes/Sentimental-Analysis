import os
import json
class Database:
    def __init__(self, name="db"):
        self.name = name
        os.makedirs(name, exist_ok=True)
    def create_table(self, table_name):
        path = os.path.join(self.name, table_name+".json")
        if os.path.exists(path):
            return "The table already exists"
        table_data = {"columns": ["id"], "rows": []}

        with open(path, "w") as f:
            json.dump(table_data,f, indent=4)
        return "Table created successfully"
    
    def add_columns(self, table_name, columns):
        path = os.path.join(self.name, table_name + ".json")
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            return f"There is no table with the name {table_name}"
        table_data = json.load(open(path))
        table_data["columns"].extend(columns)
        with open(path, "w") as f:
            json.dump(table_data, f, indent=4)
        return "Columns added successfully"
    def insert_row(self, table_name, rows: dict[str,str|int]):
        try:
            path = os.path.join(self.name, table_name + ".json")
            if not os.path.exists(path) or os.path.getsize(path) == 0:
                raise ValueError("The table doesn't exist.")
            table_data = json.load(open(path))
            rows["id"] = len(table_data["rows"]) + 1

            columns = table_data["columns"]
            if not all(row in columns for row in rows.keys()):
                raise ValueError("Invalid row data.")
            table_data["rows"].append(rows)
            with open(path, "w") as f:
                json.dump(table_data, f, indent=4)
            return "Row added successfully."
        except ValueError as e:
            return f"An error occurred while trying to add your data: {e}"

    def select(self, table_name, filters, limit=None):
        path = os.path.join(self.name, table_name + ".json")
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            raise ValueError("The table doesn't exist.")

        table_data = json.load(open(path))["rows"]

        # Filter rows based on the provided filters
        rows = [row for row in table_data if all(row[key] == value for key, value in filters.items())]

        # Apply limit if specified
        if limit is not None:
            rows = rows[:limit]

        return rows
    def update(self,table_name,data,where= None):
        if where is None:
            where = {}
        path = os.path.join(self.name,table_name+".json")
        if not os.path.exists(path) or os.path.getsize(path)==0:
            raise ValueError("")
        table_data = json.load(open(path))
        table_rows= table_data["rows"]
        for row in table_rows:
            if all(row.get(k)==v for k,v in where.items()):
                 for key, value in data.items():
                     if key in row:
                         row[key] = value
                #  table_rows[row["id"]-1] = row
        table_data["rows"] = table_rows
        with open(path, 'w') as f:
            json.dump(table_data,f, indent=4)
db1 = Database("db1")
db1.create_table("users")
db1.add_columns("users",["username","password"])
db1.insert_row("users",{
               "username":"kal","password":"pas123"
               })

db1.update("users",{"username":"alice13"},{"id":1})