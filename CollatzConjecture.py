#  Write a function that returns the number of steps it takes to reach 1 using the Collatz rules:- If n is even, divide by 2.- If n is odd, n = 3 * n + 1.


def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)  # Divide by 2 if n is even and convert to int
        else:
            n = 3 * n + 1
        steps += 1
    return steps



# Example usage:
print(collatz_steps(6))  # Output: 8 
print(collatz_steps(19)) # Output: 20 