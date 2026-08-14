class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        tab = [0]*26
        for i in range(len(s)):
            tab[ord(s[i])-ord('a')] += 1
            tab[ord(t[i])-ord('a')] -= 1
        
        for val in tab:
            if val!=0:
                return False
        return True