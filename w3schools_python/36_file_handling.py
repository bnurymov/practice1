# Python File Handling

# Write to file
with open("/tmp/example.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Python file handling is easy.\n")

# Read entire file
with open("/tmp/example.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("/tmp/example.txt", "r") as f:
    for line in f:
        print(line.strip())

# Append to file
with open("/tmp/example.txt", "a") as f:
    f.write("Added a new line.\n")

# Check if file exists
import os
print("File exists:", os.path.exists("/tmp/example.txt"))

# Delete file
# os.remove("/tmp/example.txt")
