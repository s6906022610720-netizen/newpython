# Example of membership operators

# List of fruits
fruits = ["apple", "banana", "cherry"]

# Using 'in' operator
print("banana" in fruits) # true, since "banana" is in the list
print("orange" in fruits) # false, since "orange" is not in the list

# Using 'not in' operator
print("grape" not in fruits) # true, since "grape" is not in the list
print("apple" not in fruits) # false, since "apple" is in the list

# String example
sentence = "the quuick brown fox jumps over the lazy dog"
print("fox" in sentence) # true, since "fox" is in the sentence
print("cat" not in sentence) # true, since "cat" is not in the