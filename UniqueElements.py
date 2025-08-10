#  Write a function that returns True if all elements in a list are unique, otherwise False


def all_unique(list):
    # Go through each element in the list
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            # If any two elements are the same, return False
            if list[i] == list[j]:
                return False
    # If no duplicates were found, return True
    return True

# Example usage:
print(all_unique([1, 2, 3, 4]))  # Output: True
print(all_unique([1, 2, 3, 2]))  # Output: False
