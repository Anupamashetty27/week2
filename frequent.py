def find_most_frequent_element_manual(data_list):
    """
    Finds the most frequent element in a list using a manual dictionary count.
    Returns the element. If the list is empty, returns None.
    If there are multiple elements with the same highest frequency,
    this function returns one of them (typically the one encountered first
    when iterating through the dictionary keys after populating it).
    """
    if not data_list:
        return None

    frequency_dict = {}
    for item in data_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1

    # Find the item with the maximum frequency
    # You can also do this with:
    # most_frequent = max(frequency_dict, key=frequency_dict.get)
    # However, the loop below is more explicit for understanding.

    most_frequent_item = None
    max_count = -1 # Initialize with a value lower than any possible count

    for item, count in frequency_dict.items():
        if count > max_count:
            max_count = count
            most_frequent_item = item

    return most_frequent_item

# Example Usage (using the same lists as above):
print(f"\n--- Manual Method ---")
my_list1 = [1, 2, 2, 3, 4, 2, 5, 2, 6, 1, 2]
my_list2 = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

print(f"The list is: {my_list1}")
print(f"Most frequent element: {find_most_frequent_element_manual(my_list1)}") # Output: 2

print(f"\nThe list is: {my_list2}")
print(f"Most frequent element: {find_most_frequent_element_manual(my_list2)}") # Output: 'apple'