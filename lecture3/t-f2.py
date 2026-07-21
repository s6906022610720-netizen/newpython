# Example of the identity operater

# Two varibles pointing to the same object
a = [1, 2, 3]
b = a

# Two varibles pointing to different objects with the same value
c = [1, 2, 3]  
d = [1, 2, 3]

# Using the identity operator
print(a is b)  # True, because a and b point to the same object
print(a is c)  # False, because a and c point to different objects  
print(c is d)  # False, because c and d point to different objects

# Using the equality operator for comparison
print(a == b)  # True, since a and b have the same value
print(a == c)  # True, since a and c have the same value