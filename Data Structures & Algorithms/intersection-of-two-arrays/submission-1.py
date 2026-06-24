class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums2.sort()

        
        for index in range(len(nums1)): 
            target = nums1[index]
            if target in result: 
                continue 
            lo, hi = 0, len(nums2) - 1
            while lo <= hi: 
                mid = (lo + hi) // 2 
                if nums2[mid] == target: 
                    result.append(nums2[mid])
                    break 
                elif nums2[mid] > target: 
                    hi = mid - 1 
                else: 
                    lo = mid + 1 
            
        return result
