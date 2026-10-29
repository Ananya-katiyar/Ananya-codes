from collections import Counter
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        n = len(matches)
        winner = []
        loser = []
        for w, l in matches:
            winner.append(w)
            loser.append(l)
        ans1 = []
        ans2 = []
        ans1.extend(list(set(winner) - set(loser)))
        ans1.sort()
        freq = Counter(loser)
        for player, losses in freq.items():
            if losses == 1:
                ans2.append(player)
        ans2.sort()
        return [ans1, ans2]
        