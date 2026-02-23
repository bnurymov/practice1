n = input()
word = list(n)
m = len(n)
for i in range(m - 1, 0, -1):
    if(i > m - 1 - i):
        print(word[i], end = "")
for i in range(m):
    if(i == m - 1 - i):
        print(word[i], end = "")
for i in range(m - 1, -1, -1):
    if(i < m - 1 - i):
        print(word[i], end = "")
    
        

