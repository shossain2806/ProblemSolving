# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []

        while len(nums1) != 0 or len(nums2) != 0:
            # first array empty
            if len(nums1) == 0:
                element = nums2.pop(0)
                merged.append(element)
            
            # second array empty
            elif  len(nums2) == 0:
                element = nums1.pop(0)
                merged.append(element)
            
            # array's are not empty
            else:
                if nums1[0] == nums2[0]:
                    element1 = nums1.pop(0)
                    element2 = nums2.pop(0)
                    merged.append(element1)
                    merged.append(element2)
                elif nums1[0] < nums2[0]:
                    element = nums1.pop(0)
                    merged.append(element)
                else:
                    element = nums2.pop(0)
                    merged.append(element)

        mergedLen = len(merged)
       
        if mergedLen == 0:
            return float(0)
        
        if mergedLen % 2 == 0:
            median = int(mergedLen / 2)
            result = (merged[median - 1] + merged[median]) / 2.0
            return float(result)
        else:
            median = int(mergedLen / 2)
            result = merged[median]
            return float(result)
        
sol = Solution()
print(sol.findMedianSortedArrays([1, 3],[2]))
print(sol.findMedianSortedArrays([1,2], [3,4]))
print(sol.findMedianSortedArrays([0,0], [0,0]))
print(sol.findMedianSortedArrays([], [1]))
print(sol.findMedianSortedArrays([2], []))