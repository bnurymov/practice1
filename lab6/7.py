n = int(input())
words = input().split()
x = max(words, key = len)
print(x)