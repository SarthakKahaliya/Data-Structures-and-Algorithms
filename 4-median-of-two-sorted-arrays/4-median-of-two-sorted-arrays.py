class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        
        m = len(nums1)
        n = len(nums2)
        
        mergedArray = []
        
        while True:
            if p1 >= m and p2 >= n:
                break;
                
            if p1 < m and p2 < n: 
                if nums1[p1] >= nums2[p2]:
                    mergedArray.append(nums2[p2])
                    p2 += 1
                    
                else:
                    mergedArray.append(nums1[p1])
                    p1 += 1
            else:
                if p1 < m:
                    mergedArray.append(nums1[p1])
                    p1 += 1

                if p2 < n:
                    mergedArray.append(nums2[p2])
                    p2 += 1

                        
        if len(mergedArray) % 2 == 0:
            a = len(mergedArray) // 2
            b = a - 1
        else:
            a = (len(mergedArray) // 2)
            b = a
        
        
        return float((mergedArray[a] + mergedArray[b])/2)
            
            