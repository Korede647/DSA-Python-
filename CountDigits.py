# Write a function that returns the number of digits in a number, without converting it to a string


def count_digits(n):
    if n == 0:
        return 1  

    count = 0
    is_negative = n < 0
    n = abs(n)

    while n > 0:
        n = int(n / 10)
        count += 1

    return count if not is_negative else count + 1  # Include sign for negative numbers


# Example usage:
print(count_digits(12345))  # Output: 5
print(count_digits(-20458)) # Output: 6
print(count_digits(0))      # Output: 1