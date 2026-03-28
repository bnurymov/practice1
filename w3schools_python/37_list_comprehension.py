# Python List Comprehension

# Basic comprehension
squares = [x**2 for x in range(10)]
print(squares)

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# Nested comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for row in matrix:
    print(row)

# Flatten nested list
nested = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in nested for x in row]
print(flat)

# Dict comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(word_lengths)
