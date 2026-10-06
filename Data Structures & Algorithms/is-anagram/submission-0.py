class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = sorted(s)
        n = sorted(t)
        if (n == m):
            return True
        else:
            return False