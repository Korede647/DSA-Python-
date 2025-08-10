#  Write a function to find the second largest number in a list without using sorting.


def second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements to find the second largest

    first, second = numbers[0], numbers[1]
    if second > first:
        first, second = second, first

    for num in numbers[2:]:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
            
    return second



# Example usage:
print(second_largest([3, 1, 4, 4, 5, 2]))  # Output: 4
print(second_largest([10, 20, 30, 40]))      # Output: 30
