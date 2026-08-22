class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        
        lst = [[] for _ in range(len(nums) + 1)]
        for key, value in mp.items():
            lst[value].append(key)
        ans = []
        for i in range(len(lst) - 1, -1,-1):
            if len(lst[i]) != 0:
                temp = lst[i]
                for j in range(len(temp)):
                    ans.append(temp[j])
                if len(ans) >= k:
                    break

        return ans[:k]

