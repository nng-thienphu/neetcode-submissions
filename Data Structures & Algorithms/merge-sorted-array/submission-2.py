class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        i = m - 1  # array 1 
        j = n - 1  # array 2

        while i >= 0 and j >= 0: 
            # compare the current element of array 1 
            # vs the current element of array 2
            if nums1[i] > nums2[j]: 
                # then insert to the arr 1
                # the element that bigger (from nums 1)
                nums1[last] = nums1[i]
                i -= 1 
            
            else: 
                # then insert to the arr 1
                # the element that bigger (from nums 2)
                nums1[last] = nums2[j]
                j -= 1
            last -= 1 
        
        # if nums 2 still have number leftovers, copy all of them to -> nums 1
        while j >= 0: 
            nums1[last] = nums2[j] 
            j -= 1
            last -= 1 


        