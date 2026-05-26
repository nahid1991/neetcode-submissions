class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = {}
        for num in nums:
            if num not in contains:
                contains[num] = True
            else:
                return True
        return False