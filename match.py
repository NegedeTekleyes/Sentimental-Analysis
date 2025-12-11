# # day = int(input('Enter day:'))
# # month = int(input('Enter month: '))
# # match day:
# #     case 1 | 2 | 3 |4 | 5 if month == 2 :
# #         print('It is weekday in Feburary')
# #     case 6 | 7:
# #         print('weekend')
# #     case _:
# #         print('Unknown')

# # Given variables
# # pet = "dog"
# # age = 1

# # # Use a match statement to classify the pet
# # match (pet, age):
# #     case ("dog", n) if n < 2:
# #         pet_type = "puppy"
# #     case ("dog", n) if n >= 2:
# #         pet_type = "adult dog"
# #     case ("cat", n) if n < 2:
# #         pet_type = "kitten"
# #     case ("cat", n) if n >= 2:
# #         pet_type = "adult cat"
# #     case _:
# #         pet_type = "other pet"

# # # Print the result
# # print(pet_type)

# # list comphresion
# # square = [x**2 for x in range(10)]
# # print(square)

# numbers = [1,2,3,4,5,6,7,8,9]
# evens = ["even" if num% 2 == 0 else "odd" for num in numbers ]
# print(evens)
# # lists comprehension in python
# from datetime import date
# users = [ 
#     {1,  "Alice ",  21},
#     {2,  "bob",  21},
#     {3,  " Alice",  23},
#      ]
# # example if you have a name list like this below
# current_year = date.today().year
# # names = [user["name"].strip() for user in users] # stip removes space when type
# # print(names)
# # names = [{user["name"]:current_year - user["age"] for user in users}] # stip removes space when type
# # print(names)
# flatten_list = []
# for user in users:
#     for value in user:
#         flatten_list.append(value)

# flatten_list = [value for user in users for value in user]
# print(flatten_list)


# function in pyhton
def func(num1,num2,num3):
    res = num1 *num2 /num3
    return res
print(func( 4,5,6))
