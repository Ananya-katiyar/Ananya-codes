class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        slst = [0] * 26
        plst = [0] * 26
        for i in range (len(p)):
            idx = ord(p[i]) - ord('a')
            plst[idx] += 1
        l = 0
        r = 0
        while r < len(s):
            idx = ord(s[r]) - ord('a')
            slst[idx] += 1
            if (r - l + 1) > len(p):
                idx1 = ord(s[l]) - ord('a')
                slst[idx1] -= 1
                l += 1
            if (r - l + 1) == len(p) and slst == plst:
                ans.append(l)
            r += 1
        return ans



        
