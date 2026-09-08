fruits = {"apple" , "banana" , "cherry"}

# fruits.add("orange")  #{'apple', 'cherry', 'banana', 'orange'}
# print(fruits)

# fruits.remove("banana")  #{'apple', 'cherry', 'orange'}
# print(fruits)

# fruits.discard("grape")  #{'apple', 'cherry', 'orange'}
# print(fruits)

remove_item = fruits.pop()
print(remove_item)
print(fruits)  #{'cherry', 'orange'}

fruits.clear()
print(fruits)  #set()