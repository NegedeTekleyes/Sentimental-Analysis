import sys

if len(sys.argv) < 2:
    print("Usage: python lists.py create_db table_name")
elif sys.argv[1] == 'create_db':
    db = []
    table_cols = []
    
    table_name = input("Enter the table name: ")
    number_of_cols = int(input("Enter number of columns: "))
    
    for i in range(number_of_cols):
        col_name = input(f"Enter column name for column {i + 1}: ")
        table_cols.append(col_name)
    
    print(f"Table '{table_name}' created with columns: {table_cols}")

else:
    print('Invalid command')