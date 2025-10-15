"""
Week 4 Assignment - Part 2, Task 1: AI-Powered Code Completion

Task: Write a Python function to sort a list of dictionaries by a specific key.
This file contains the manual implementation for comparison against AI-generated code.
"""

def sort_list_of_dicts(data: list, key: str, reverse: bool = False) -> list:
    """
    Sorts a list of dictionaries by the value associated with a specified key.

    :param data: The list of dictionaries to sort.
    :param key: The dictionary key to sort by.
    :param reverse: If True, sort in descending order. Default is False (ascending).
    :return: The sorted list of dictionaries.
    """
    # Using the sorted() built-in function with a lambda function for the key
    # This is generally the most efficient and Pythonic way to perform this sort.
    return sorted(data, key=lambda d: d.get(key), reverse=reverse)

# Example Usage
employees = [
    {'name': 'Alice', 'salary': 60000, 'age': 30},
    {'name': 'Bob', 'salary': 80000, 'age': 45},
    {'name': 'Charlie', 'salary': 60000, 'age': 25},
    {'name': 'David', 'salary': 95000, 'age': 35}
]

print("Original List:")
print(employees)

print("\nSorted by salary (Ascending):")
sorted_by_salary = sort_list_of_dicts(employees, 'salary')
print(sorted_by_salary)

print("\nSorted by age (Descending):")
sorted_by_age_desc = sort_list_of_dicts(employees, 'age', reverse=True)
print(sorted_by_age_desc)
