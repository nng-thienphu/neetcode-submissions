class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)
        if n <= 1:                      # 0 or 1 element = already sorted (base case)
            return pairs

        mid = n // 2
        left = self.mergeSort(pairs[:mid])    # sort left half
        right = self.mergeSort(pairs[mid:])   # sort right half
        return self.merge(left, right)        # merge two sorted halves

    def merge(self, left: List[Pair], right: List[Pair]) -> List[Pair]:
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:   # <= not < — this is what makes it STABLE
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])    # one of these is empty; the other is leftovers, already sorted
        res.extend(right[j:])
        return res