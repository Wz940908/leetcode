class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for item in range(len(S)):
            for item2 in range(len(J)):
                if J[item2] == S[item]:
                    count+=1
        return count
