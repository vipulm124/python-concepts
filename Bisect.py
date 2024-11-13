
from bisect import bisect, bisect_left, bisect_right

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