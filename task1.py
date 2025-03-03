def fibonacci_generator(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage: Print the first 10 Fibonacci numbers
num_terms = 10
fib = fibonacci_generator(num_terms)
for number in fib:
    print(number)
