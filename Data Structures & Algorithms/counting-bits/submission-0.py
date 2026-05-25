class Solution:
    # KEY: 
    # Any number i can be split as "its highest 1-bit" plus "everything below that bit." 
    # The highest 1-bit contributes exactly 1 to the count, 
    # and the part below it is some smaller number whose answer we've already computed. 
    # So arr[i] = 1 + arr[i - p], where p is the largest power of 2 that's ≤ i. 

    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n+1) 
        # arr[1] = 1 
        # arr[2] = 1 

        for i in range(1, n+1): 
            p = int(math.log2(i))
            arr[i] = 1 + arr[i-2**p]
            # print(f"number {i}, power {p}, arr {arr[i-2**p]}")

        
        return arr