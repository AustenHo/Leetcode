# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = min([len(s) for s in strs])
        ret = ""
        for i in range(l):
            for j in range(len(strs)-1):
                if strs[j+1][i] != strs[j][i]:
                    return ret
            ret += strs[0][i]
        return ret