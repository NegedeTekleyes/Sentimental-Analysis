# tuple is immutable( can not change or update)
fruit1 = ("orenge","mango","banana",1,True,0)
print(fruit1)
print(type(fruit1))
# if you update tuple use indirect way throurh  means changing the tuple to lists
list1=list(fruit1)
list1[0]=["lemon"]
print(type(list1))
# fruit2 =("lemon") # this is string  out put type of fruit2 <class 'str'>
fruit2 =("lemon",) # when we add , in the string it changes to tuple out put type of fruit2 <class 'tuple'>
# print("type of fruit2", type(fruit2))
# fruit1 = fruit1 + fruit2
if fruit1[-1]:
    print(fruit1)

else:
    print("There is no tuple")
