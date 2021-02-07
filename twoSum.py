from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int):
        output = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in output:
                return [output[diff],i ]
            output[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
