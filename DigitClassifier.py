#  Write a function that takes an integer and returns:- 'Even and divisible by 3' if it's both even and divisible by 3,- 'Even' if only even,- 'Odd' if it's odd,- 'Zero' if it’s 0


def classify_integer(n):
    if n == 0:
        return 'Zero'
    elif n % 2 == 0:
        if n % 3 == 0:
            return 'Even and divisible by 3'
        else:
            return 'Even'
    else:
        return 'Odd'

# Example usage:
print(classify_integer(6))  # Output: Even and divisible by 3
print(classify_integer(17)) # Output: Odd
print(classify_integer(52)) # Output: Even