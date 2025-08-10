#  Write a function that returns the number of steps it takes to reach 1 using the Collatz rules:- If n is even, divide by 2.- If n is odd, n = 3 * n + 1.


def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


# Example usage:
print(collatz_steps(6))  # Output: 8 (6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1)
print(collatz_steps(19)) # Output: 20 (19 -> 58 -> 29 -> 88 -> 44 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1)