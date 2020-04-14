#bubble
def bubble_sort(nums):
swapped = True
while swapped:
swapped = False
for i in range(len(nums) - 1):
if nums[i] > nums[i + 1]:
nums[i], nums[i+1] = nums[i+1], nums[i]
swapped = True
import random
arry = [random.randint(0, 2600) for i in range(2600)]
bubble_sort(arry)
print(arry)
