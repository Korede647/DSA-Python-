#  Write a function that takes a number and returns its reverse without converting it to a string

def reverse_number(n):
    reversed_num = 0
    is_negative = n < 0
    n = abs(n)

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return -reversed_num if is_negative else reversed_num

# Example usage:
print(reverse_number(1234))  # Output: 4321
print(reverse_number(5697)) # Output: 7965