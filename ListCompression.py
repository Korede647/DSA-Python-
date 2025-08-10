#  Write a function that takes a list of integers and returns a new list with all even numbers doubled and odd numbers removed


def compress_list(numbers):
    compressed = []
    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            compressed.append(num * 2)  # Double the even number
    return compressed


# Example usage:
print(compress_list([1, 2, 3, 4, 5, 6]))  # Output: [4, 8, 12]
print(compress_list([10, 15, 20, 25]))    # Output: [20, 40]