class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        mp = {}
        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]]+1)
            mp[s[r]] = r
            res = max(res, r-l+1)
        return res
        # Create an empty res
        # Start the l = 0
        # Create an empty map
        # loop through r
            # if the char is in the map
                # update the l
            # add the char into the map
            # updat the res
        # return the res