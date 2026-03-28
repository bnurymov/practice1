# Python Arrays (using list as array)
# Python doesn't have built-in arrays; use lists or array module

from array import array

# Array of integers
arr = array('i', [1, 2, 3, 4, 5])
print(arr)
print(arr[0])

arr.append(6)
arr.remove(3)
print(arr)

# Using list as array
nums = [10, 20, 30, 40]
print(nums[1])
nums.insert(2, 25)
print(nums)
