class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxLength = len(strs[0])
        for word in strs:
            if len(word) < maxLength:
                maxLength = len(word)
        prefix = ""
        for i in range(0,maxLength):
            letter = strs[0][i]
            for word in strs:
                if word[i] != letter:
                    return prefix
            prefix += letter
        return prefix