class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) < len(set2):
            return filter(lambda x: x in set2, set1)
        else:
            return filter(lambda x: x in set1, set2)