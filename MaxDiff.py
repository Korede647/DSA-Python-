#  Write a function that returns the maximum difference between any two elements in a list, with the larger element coming after the smaller one


def max_diff(numbers):
    if len(numbers) < 2:
        return 0  # No elements to find a difference

    min_value = numbers[0]
    max_difference = 0
    
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
        else:
            max_difference = max(max_difference, num - min_value)
    
    return max_difference


# Example usage:
print(max_diff([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Output: 8 (9 - 1)
print(max_diff([10, 20, 30, 40]))              # Output: 30 (40 - 10)