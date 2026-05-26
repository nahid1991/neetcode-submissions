class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumNums = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in sumNums:
                return [sumNums[complement], i]
            sumNums[nums[i]] = i



