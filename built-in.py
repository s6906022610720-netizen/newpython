# Example list
numbers = [4, 2, 9, 1, 5, 6]

length = len(numbers)
print(f"Lenght of the list: {length}")

total_sum = sum(numbers)
print(f"Sum of all elemnts: {total_sum}")

max_value = max(numbers)
print(f"Maximum value : {max_value}")

min_value = min(numbers)
print(f"Minimum value : {min_value}")

sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")

bool_list = [False, True, False]
any_true = any(bool_list)

all_true = all(bool_list)
print(f"Are all elements true? {all_true}")

string = "hello"
char_list = list(string)
print(F"List of characters: {char_list}")

reversed_numbers = list(reversed(numbers))
print(f"Reversed list: {reversed_numbers}")

enumerted_numbers = list(enumerate(numbers))
print(f"Enumerted list: {enumerted_numbers}")