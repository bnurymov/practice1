# Python Generators
# Memory-efficient iterators using yield

def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up(5)
print(next(gen))  # 1
print(next(gen))  # 2

for num in count_up(5):
    print(num)

# Generator expression
squares = (x**2 for x in range(10))
print(list(squares))

# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(10)])
