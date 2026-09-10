class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        first = 0
        second = len(s)-1

        while first<second:
            if not s[first].isalnum():
                first += 1
                continue
            if not s[second].isalnum():
                second -= 1
                continue
            if first == second:
                return True
            if s[first]!=s[second]:
                return False
            first+=1
            second -=1

        return True