# Python Lambda Functions
# Anonymous, one-line functions

square = lambda x: x ** 2
print(square(5))   # 25

add = lambda x, y: x + y
print(add(3, 4))   # 7

# Lambda with sorted
people = [("Alice", 30), ("Bob", 25), ("Carol", 35)]
people.sort(key=lambda p: p[1])
print(people)

# Lambda with map/filter
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(doubled)
print(evens)
