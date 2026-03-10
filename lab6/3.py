n = int(input())
word = input().split()
enuword = list(enumerate(word))
for i in range(n):
    print(enuword[i][0], end = "")
    print(":", end = "")
    print(enuword[i][1], end = " ")
