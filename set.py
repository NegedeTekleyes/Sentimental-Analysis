# sets in python not stire duplicate values unlike list
letters1 = {'a','b','c','d',1, True}
letters2 = {'b','b','e','d',0, False}
# letters3 = letters1.update(letters2)
letters3 = letters1 | letters2
letters3 = letters1 & letters2


print(letters3) # since 1 and True are same the out put is {1, 'a', 'd', 'c', 'b'}