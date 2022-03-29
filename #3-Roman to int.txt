class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
}
        n=len(s)
        total = 0
        for i in range(n):
            if i==n-1 or romanDict[s[i]] >= romanDict[s[i+1]]:
                total = total + romanDict[s[i]]
            else:
                total = total - romanDict[s[i]]
        return total