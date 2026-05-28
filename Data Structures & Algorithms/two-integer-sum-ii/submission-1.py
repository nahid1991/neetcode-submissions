class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIdx = 0
        rightIdx = len(numbers) - 1

        while leftIdx < rightIdx:
            smallerNumber = numbers[leftIdx]
            largerNumber = numbers[rightIdx]

            potentialMatch = smallerNumber + largerNumber

            if potentialMatch > target:
                rightIdx -= 1
            elif potentialMatch < target:
                leftIdx += 1
            else:
                return [leftIdx+1, rightIdx+1]
        return []