#  Given a list of numbers from 1 to n with one number missing, find the missing number


def find_missing_number(numbers, n):
    total = n * (n + 1) // 2  # Sum of first n natural numbers
    current_sum = sum(numbers)  # Sum of the given numbers
    return total - current_sum  # The missing number


# Example usage:
print(find_missing_number([1, 2, 4, 5], 5))  # Output: 3
print(find_missing_number([1, 3, 4, 5, 6], 6))  # Output: 2