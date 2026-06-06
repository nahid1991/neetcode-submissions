class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        merged = []
        idxOne, idxTwo = 0, 0
        
        while len(merged) <= (total_len // 2):
            if idxOne < len(nums1) and (idxTwo >= len(nums2) or nums1[idxOne] <= nums2[idxTwo]):
                merged.append(nums1[idxOne])
                idxOne += 1
            elif idxTwo < len(nums2):
                merged.append(nums2[idxTwo])
                idxTwo += 1
            else:
                break

        if total_len % 2 == 1:
            return float(merged[total_len // 2])
        else:
            return (merged[-1] + merged[-2]) / 2.0