from typing import List


class Solution:
    def checkIfIncreasing(self, nums):
        length = len(nums)
        isIncreasing = True
        for i in range(length-1):
            if nums[i+1] <= nums[i]:
                isIncreasing = False
        
        return isIncreasing

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        k = 2
        length = len(nums)
        maxVal = 0
        # moveAhead = False
        print(f'Length ofnums: {length}')

        for i in range(length-1):
            print(f'value of i: {i}')
            print(f'maxVal: {maxVal}')
            # moveAhead = False
            while k <= int((length-i)/2):
                nums1 = nums[i:i+k]
                nums2 = nums[i+k:i+k+k]
                if self.checkIfIncreasing(nums1) and self.checkIfIncreasing(nums2):
                    maxVal = max(maxVal, len(nums1))
                k += 1
            k = 2
            
        return k



nums = [2,5,7,8,9,2,3,4,3,1]
sol = Solution()
sol.maxIncreasingSubarrays(nums=nums)