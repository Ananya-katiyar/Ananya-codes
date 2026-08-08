class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapST = {}
        mapTS = {}

        for x,y in zip(s,t):
            if x in mapST and mapST[x] != y:
                return False
            if y in mapTS and mapTS[y] != x:
                return False
            mapST[x] = y
            mapTS[y] = x
        return True   
