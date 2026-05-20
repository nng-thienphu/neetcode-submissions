class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {} 
        if len(s) != len(t) :
            return False

        for i in range(len(s)): 
            if s[i] in hash_s: 
                hash_s[s[i]] += 1
            else: 
                hash_s[s[i]] = 1

            if t[i] in hash_t: 
                hash_t[t[i]] += 1
            else: 
                hash_t[t[i]] = 1

        # then compare two hash map 
        return Counter(s) == Counter(t)
