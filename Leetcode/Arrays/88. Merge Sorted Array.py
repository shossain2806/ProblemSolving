class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr = 0
        for index in range(m, len(nums1)):
            nums1[index] = nums2[curr]
            curr += 1
        nums1.sort()
                
    ## from back no need space
    def alternateMerge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        
        p1 = 0
        p2 = 0
        
        for p in range(m + n):
            
            if p1 < m and p2 < n:
                if nums1_copy[p1] < nums2[p2]:
                    nums1[p] = nums1_copy[p1]
                    p1 += 1
                else:
                    nums1[p] = nums2[p2]
                    p2 += 1
            elif p1 < m:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1