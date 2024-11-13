
# this just provided the index, where the no. should be added in sorted array, it does not add the value
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right

def bisect_it(nums, num):
    print(bisect(nums, num))

def bisect_lft(nums, num):
    print(bisect_left(nums, num))

def bisect_rght(nums, num):
    print(bisect_right(nums, num))

nums = [1,2,3,4,4,4,5,5,6]
bisect_it(nums, 5)

bisect_lft(nums, 5)

bisect_rght(nums, 5)


# TO add the value, we use insort

def display(nums):
    for i in nums:
        print(i)
    print("=======")

def insort_it(nums, num):
    display(nums)
    insort(nums, num,7 ,8)
    display(nums)

# similary insort_left and insert_right works


insort_it(nums, 4)