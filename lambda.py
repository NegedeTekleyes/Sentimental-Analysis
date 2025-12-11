add = lambda a, b: a + b
print(add(4,56))

# let we have alist and you want multiple by 2 you can do with for loop but it is not effeicent so we use lambda
numbers = [1,2,3,4,5,7,8]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i]*2
#     print(numbers)
# insteda of this lets craee another list
# numbers2 = list(map(lambda n: n*2, numbers))
# ኢፍፍ ዮኡ ነእድ ፊልተር 
numbers2 = list(filter(lambda n: n%2 == 0, numbers))
print(numbers2)
    
