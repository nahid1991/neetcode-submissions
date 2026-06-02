class Solution:
    def search(self, nums: List[int], target: int) -> int:
        startIdx = 0
        endIdx = len(nums) - 1

        while startIdx <= endIdx:
            num1 = nums[startIdx]
            num2 = nums[endIdx]
            middleIdx = (startIdx+endIdx) // 2
            midNum = nums[middleIdx]

            if target > midNum:
                startIdx = middleIdx + 1
            elif target < midNum:
                endIdx = middleIdx - 1
            else:
                return middleIdx

        return -1