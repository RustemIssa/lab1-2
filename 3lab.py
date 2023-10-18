user_input = input("Enter a string without whitespaces: ")
user_input = user_input.strip()  
user_tuple = tuple(user_input)
print("User input as a tuple:", user_tuple)


input_tuple = ('t', 'h', 'i', 's', 'i', 's', 'a', 't', 'u', 'p', 'l', 'e')
output_string = ''.join(input_tuple)
print("Tuple converted back to string:", output_string)


tuple_a = (1,2,3,4,5,6,7)
tuple_b = (5,6,7,9,7,1,10,10)
midpoint = len(tuple_a) // 2
concatenated_tuple = tuple_a[:midpoint] + tuple_b[midpoint:]
print("Concatenated Tuple:", concatenated_tuple)


input_tuple = (1, 2, 'apple', 1, 'banana', 'apple', [3, 4], [3, 4], 'apple')
element_counts = {}
for element in input_tuple:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1
result_tuple = tuple((element, count) for element, count in element_counts.items())
print("Element counts:", result_tuple)


int_tuple = (1, 2, 3, 4, 5)
str_tuple = ('apple', 'banana', 'cherry', 'date')
mixed_tuple = (1, 'apple', [3, 4], {'name': 'John', 'age': 30})
print("Tuple with integers:", int_tuple)
print("Tuple with strings:", str_tuple)
print("Tuple with mixed data types:", mixed_tuple)


user_input = input("Enter a string without whitespaces: ")
user_input = user_input.strip() 
input_set = {char for char in user_input}
print("Created set is:")
print(input_set)


set_a = {1,2,3,4,5}
set_b = {5,7,8,9,2,10}
difference_set = set_a - set_b
print("Set A:", set_a)
print("Set B:", set_b)
print("Difference Set (Set A - Set B):", difference_set)


set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
set_A.difference_update(set_B)
print(set_A)


set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}
for element in set_A.copy():
    if element in set_C:
        set_A.remove(element)
        set_B.add(element)
set_C.update(set_A)
print("Updated set_C =", set_C)


from itertools import combinations
A = {1, 2, 3, 4, 5, 6}
n = 3
m = 5
combinations_list = []
if n <= len(A):
    for _ in range(m):
        random_combination = set(combinations(A, n))
        while random_combination in combinations_list:
            random_combination = set(combinations(A, n))
        combinations_list.append(random_combination)
print(combinations_list)


from itertools import groupby
cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]
cars_list.sort(key=lambda x: x[0])
manufacturer_groups = groupby(cars_list, key=lambda x: x[0])
for manufacturer, group in manufacturer_groups:
    models = [model for _, model in group]
    count = len(models)
    print(f"{manufacturer} {count}")
    for model in models:
        print(f"- {model}")



input_tuple = (5, 55, 10, 1, 0, 1, 55, 77, 10, 5, 5, 55, 77)
element_counts = {}
for element in input_tuple:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1
max_count = max(element_counts.values())
min_count = min(element_counts.values())
most_popular = [element for element, count in element_counts.items() if count == max_count]
least_popular = [(element, count) for element, count in element_counts.items() if count == min_count]
frequent_elements = [(element, count) for element, count in element_counts.items() if list(element_counts.values()).count(count) > 1]
print("Elements and their occurrences:")
print([(element, count) for element, count in element_counts.items()])
print("The most popular element:", most_popular if len(most_popular) > 1 else "no most popular element")
print("The least popular element:", least_popular[0] if len(least_popular) == 1 else "no least popular element")
print("The frequent elements:", frequent_elements)
