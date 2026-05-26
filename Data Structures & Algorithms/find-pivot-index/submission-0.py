class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSums = [0] * len(nums)
        prefixSums[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSums[i] = nums[i] + prefixSums[i - 1]

        for i in range(len(nums)):
            leftSum = prefixSums[i - 1] if i > 0 else 0
            rightSum = prefixSums[len(nums) - 1] - prefixSums[i]
            if leftSum == rightSum:
                return i
        return -1
