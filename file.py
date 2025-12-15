# file = open('test.txt','a') # you change the second argument as you want in money tasks write 'w
# # , read append and so on
# file.write("Hi there! How is the course so far?")
# file.close()

# # to read a file
# file = open('test.txt', 'r')
# data = file.readline()
# print(data)
# file.close()

# Now here's the thing.

# Opening a file and then remembering to close it every single time can be a little repetitive.

# There's actually a better way to do it in Python, and that's by using what's called a context manager

# with the word with.

# What this does is it lets me open the file, do whatever I want with it, and once I'm done, Python

# automatically closes it for me.

# I don't even have to think about it.

# That makes the code much cleaner and less error prone.

# So for now, I'm just going to print the reading operation of the file.
# with open('test.txt','r') as file:
#     print(file.read())

# Exercise: Build Your Own Mini Database (File Edition)
# Alright, it’s time to take everything you’ve learned about files and JSON and use it to build something cool, a tiny version of a database system!

# In this challenge, you’ll simulate how databases store tables and columns, but instead of using SQL or an actual DB engine, you’ll do it entirely with Python, JSON, and files.

# import os
# import json
# class Database:
#     def __init__(self, name):
#         self.name = name

#         if os.path.exists(name):
#             raise Exception(f"Database '{name}' already exists!")
#         else:
#             os.mkdir(name)
#             print(f"Database '{name}' created.")

#     def create_table(self, table_name):
#         table_path = os.path.join(self.name, f"{table_name}.json")

#         if os.path.exists(table_path):
#             raise Exception(f"Table '{table_name}' already exists.")

#         with open(table_path, "w") as file:
#             json.dump({"columns": []}, file, indent=2)

#         print(f"Table '{table_name}' created.")

#     def add_column(self, table_name, column_name):
#         table_path = os.path.join(self.name, f"{table_name}.json")

#         if not os.path.exists(table_path):
#             raise Exception(f"Table '{table_name}' does not exist.")

#         # Read existing table data
#         with open(table_path, "r") as file:
#             data = json.load(file)

#         # Prevent duplicate columns
#         if column_name in data["columns"]:
#             raise Exception(f"Column '{column_name}' already exists.")

#         data["columns"].append(column_name)

#         # Write updated data back
#         with open(table_path, "w") as file:
#             json.dump(data, file, indent=2)

#         print(f"Column '{column_name}' added to table '{table_name}'.")

#     def show_tables(self):
#         tables = [
#             file.replace(".json","")
#             for file in os.listdir(self.name)
#             if file.endswith(".json")
#         ]
#         print("Tables:")
#         for table in tables:
#             print("-", table)
# db = Database("company_db")
# db.create_table("employees")
# db.show_tables()
# db.add_columns("employees", "id")
# db.add_columns("employees", "name")
# db.add_columns("employees", "salary")

    
# Journal Keeper
# You’ve been hired by a mysterious client who wants to keep a daily journal of their thoughts but they’re too lazy to manage the files themselves. Your job is to build a small program that takes care of their journal entries.

class Journal:
    def __init__(self,filename= "jornal.txt"):
        self.filename = filename
        # create file if it does not exist
        with open(self.filename, 'a'):
            pass
    def add_entry(self):
        entry = input("Enter your Jornal")

        # append new entry
        with open(self.filename, 'a') as file:
            file.write(entry + "\n")

        # read and display all entries
        print("\n --- Journal Entites ---")
        with open(self.filename,'r') as file:
            print(file.read())

journal = Journal()
journal.add_entry()
        