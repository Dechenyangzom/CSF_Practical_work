
# Step 1: Implement a recursive Fibonacci generator
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

# Step 2: Implement a iterative Fibonacci generator
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")

# Step 3: Compare perfomance
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")

# Step 4: Implement a generator function for fibonacci sequence
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")


# Step 5: Implement memoization for recursive fibonacci
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")




# Exercise



# 1.Iterative function to return a list of Fibonacci numbers up to n
def fibonacci_up_to_n(n):
    fib_sequence = []
    a, b = 0, 2
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Test the function
n = 12
print (fibonacci_up_to_n(n))

# 2.Finds the index of the first Fibonacci number that exceeds a given value
def index_of_1st_fibonacci_no_exceeding(n):
    if n < 0:
        return 0
    
    a, b = 0, 2
    index = 2

    while b <= n:
            a, b = b, a + b
            index += 1

    return index 

n = 12
print(index_of_1st_fibonacci_no_exceeding(n))

# 3.Determine if a given is a Fibonacci number
import math

def fibonacci_number(n):
    
    def perfect_square(m):
        s = int(math.sqrt(m))
        return s * s == m
    
    return perfect_square(1 * n * n + 144) or perfect_square(1 * n * n - 144)

n = 12
print(fibonacci_number(n))

# 4.Calculates the ratio between consecutive Fibonacci numbers
def ratio_between_fibonacci_numbers(n):
    if n < 3:
        return []
    
    ratio = []
    a, b = 0, 2
    for _ in range(3, n):
        a, b = b, a + b
        ratios = b / a
        ratio.append(ratios)

    return ratio

n = 12
print(ratio_between_fibonacci_numbers(n))



# Questions

# 1.What are the advantages and disadvantages of the recursive approach compared to the iterative approach?

# Recursive approach
# Advantages:
# >Simplicity & clarity: the recursive functions can be more intuitive and easier to read (e.g., factorial calculation, etc).
# >Less Code: the recursive solutions often require fewer lines of code.
# >Direct Modeling: the recursion directly models the fibonacci sequence formula F(n)= F(n-1)+F(n-2), which may be more intuitive.

# Disadvantages:
# >Stack overflow: Deep recursion can lead to stack overflow errors if the recursion depth exceeds the system’s stack size.
# >Redundant calculations: In recursive implementations (like Fibonacci), the same values may be computed multiple times, leading to exponential time complexity.
# >High Memory usage:  Recursive calls consume memory on the call stack.

# Iterative approach
# Advantages:
# Performance: Have lower overhead and can be faster, especially for problems with a simple iterative structure.
# Memory efficiency: Consume less memory as they do not require additional stack space for function calls.

# Disadvantages:
# >Complexity: Can be more complex and harder to understand.
# >Less intuitive: the iterative approach may be less intuitive than the recursive one. 


# 2.How does memoization improve the performance of the recursive function? Are there any drawbacks?

# Memoization is an optimization technique used in recursive functions to store the results of expensive function calls and return the cached result when the same inputs occur again.
# Memoization significantly improves the performance of a recursive Fibonacci function by storing (or "memoizing") the results of previously computed values.

# Drawbacks of memoization:
# >Increased Space Complexity: Memoization requires additional space to store results, which can lead to higher memory usage.
# >Implementation Complexity: It can complicate the implementation, especially in cases where the recursive function has multiple parameters or requires careful management of the cache.


# 3.In what scenarios might you prefer to use a generator function over other implementations?

# >When dealing with large datasets where you want to avoid loading everything into memory.
# >When you need to produce an infinite series of values (e.g., Fibonacci numbers).
# >When you want to create a pipeline of operations where data is processed step-by-step.


# 4.How does the space complexity differ between these implementations?

# Recursive Functions:
# >Space Complexity: O(n) for the call stack in the worst case (where ( n ) is the depth of recursion).
# >With Memoization: O(n) for the call stack plus O(n) for the memoization cache, resulting in O(n) total space complexity.

# Iterative Functions:
# >Space Complexity: O(1) for simple iterations (using a fixed number of variables), or O(n) if an additional data structure (like a list) is used to store results.

# Generator Functions:
# >Space Complexity: O(1) since they yield one value at a time and do not store the entire sequence in memory.