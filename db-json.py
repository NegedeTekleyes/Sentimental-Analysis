import json
import os
from datetime import datetime

class Database:
    def __init__(self, name="db"):
        self.name = name
        os.makedirs(name, exist_ok=True)

    def create_table(self, table_name):
        path = os.path.join(self.name, table_name + ".json")
        if os.path.exists(path):
            return "The table already exists"
        table_data = {
            "columns": [],
              "rows": []
              }
        with open(path, 'w') as f:
            json.dump(table_data, f, indent=4)
        return "Table created successfully"
    def add_colums(self,table_name,columns):
        path = os.path.join(self.name, table_name+".json")
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            return f"There is no table with the name {table_name}"
        table_data = json.load(open(path))
        table_data["columns"].extend(columns)
        with open(path, "w") as f:
            json.dump(table_data,f, indent=4)
            return "Columns added successfuly"
    def add_rows(self,table_name, rows: dict[str,str|int]):
        try:
            path = os.path.join(self.name,table_name+".json")
            if not os.path.exists(path) or os.path.getsize(path) == 0:
                raise ValueError("The table doesnot exist.")
            with open(path,'r') as f:
                table_data = json.load(f)
            columns = table_data["columns"]
            if not all(row in columns for row in rows.keys()):
                raise ValueError("Invalid row data")
            table_data["rows"].append(rows)
            with open(path, "w") as f:
                json.dump(table_data,f, indent=4)
            return "Row added succesfully"
    
        except ValueError as e:
            return f"An error occured while trying to add your data: {e}"
        
    def select(self,table_name,filters):
        path = os.path.join(self.name,table_name+".json")
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            raise ValueError('The table does not exist')
        table_data = json.load(open(path))['rows']
        # filter rows based on the provided filters
        rows = [row for row in table_data if  all(row[key] == value for key, value in filters.items())]
        return table_data
db1 = Database("db1")
db1.create_table("users")
db1.add_colums("users",["username","password"])
res = db1.add_rows("users",{"username": "Kal","password":"kal123"})
print(res)