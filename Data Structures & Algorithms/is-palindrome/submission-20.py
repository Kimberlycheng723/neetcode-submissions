class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            if l<r and not s[l].isalnum():
                l+=1
                continue
            if l<r and not s[r].isalnum():
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        # two pointers
        # Create two pointer (one start from the first, one start from end)
        # While l<r:
            # if l<r and s[l] is not alphanum:
                # l+=1
                # continue
            # if l<r and s[r] is not alphanum:
                #r-=1
                # continue
            # if s[l] != s[r]
                # return false
            # l += 1
            # r-=1
        # return True

     