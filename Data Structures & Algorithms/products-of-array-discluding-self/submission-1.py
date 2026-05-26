class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [0] * len(nums)
        rightProduct = [0] * len(nums)
        res = [0] * len(nums)
        leftProduct[0] = rightProduct[len(nums) - 1] = 1
        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            rightProduct[i] = rightProduct[i+1] * nums[i+1]
        for i in range(len(res)):
            res[i] = leftProduct[i] * rightProduct[i]
        return res