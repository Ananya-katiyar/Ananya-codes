class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = Counter(s)
        for key, value in mp.items():
            if value == 1:
                idx = s.find(key)
                return idx
        return -1