class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
                continue
            while l<r and not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
        # Create two pointer (one from start, one from the end of string)
        # while first < second
            # while first<second and not first.isalnum():
                # first+=1
                #continue
            # while first<Second and not second.isalnum():
                # second -= 1
                #continue
            # if s[first] != s[second]:
                # return false
            # first+=1
            # second-=1
        #return true