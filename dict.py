# car = {
#     "brand":"ford",
#     "color":"red",
#     "year":2014
# }
# # print(car["brand"])
# # print(type(car)) # <class 'dict'> 
# # # or use using dict()
# # car2 = dict(brand="Tesla",color="Brown",year="2014")
# # print(car2["year"])

# # for car in car:
# #     print(car)
# for key, value in car.items():
#     print(key, value)
# # if you want to check the brand is in the cara available or not
# if "brand" in  car:
#     print("The baran is", car["brand"])

# # if "name" in car:
# #     print("The name is", car["name"])
# if "name" not in  car:
#     car["name"] = input("Enter the car name: ")
#     print("The name is", car["name"])

# else:
#     print("The name is not found")


# create empty directory
inventory = {}
# ask user how many items they inter
num_items = int(input("How many items to add?"))

# loop to gatehr items detaile
for _ in range(num_items):
    # get item detaile fro the user
    item_name = input("Ener the item name ")
    quantity = input("Enter the quantity  ")
    category = input("Enter the category ")

    # store each item in the inventory
    inventory[item_name] = {
        "quantity": quantity,
        "category": category
    }
    print(inventory)
    for item_name, detailes in inventory.items():
        print(f"- {item_name}:{detailes['quantity']} ({category}:{detailes['category']})")


# import sys
# if len(sys.argv) < 2:
#     print("Usage: lists.py, database_name, table_name")
# elif sys.argv[1] == "create_db":
#     db = {}
#     table_cols = []
#     table_name = input("Enter table name: ")
#     db[table_name] = []
#     number_of_cols = int(input("Enter number of cols: "))

#     for i in range(number_of_cols):
#         table_cols.append(input("Enter the column name: "))
#         print(table_cols)
# else:
#     print('Invalid command')