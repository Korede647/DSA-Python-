# Write a function that checks if a number is a palindrome without converting it to a string


def is_palindrome(n):
    if n < 0:
        return False  # Negative numbers are not palindromes

    original = n
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = int(n / 10)

    return original == reversed_num


# Example usage:
print(is_palindrome(121))  # Output: True
print(is_palindrome(-121)) # Output: False
print(is_palindrome(12321)) # Output: True