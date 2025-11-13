# import sys
# if len(sys.argv) < 2:
#     print("Usage: lists.py, database_name, table_name")
# elif sys.argv[1] == "create_db":
#     db = []
#     table_name = input("Enter table name: ")
#     number_of_cols = int(input("Enter number of cols: "))



# define the class nme
class_name = "Math 101"

# define list of student
students = ['Negede','charli','cahpe']
# print class roaster
print(f'class "{class_name}" roster')
for student in students:
    print(f"- {student}")
