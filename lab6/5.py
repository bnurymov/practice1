word  = input()
words = list({"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"})
anylist = list()
for i in words:
    if i in word:
        anylist.append(True)
x = any(anylist)
if x:
    print("Yes")
else:
    print("No")