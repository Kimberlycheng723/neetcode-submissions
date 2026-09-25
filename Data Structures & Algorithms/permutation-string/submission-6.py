class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        windowCount = [0] * 26
        s1Count = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            windowCount[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == windowCount[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # add the right character
            rightIndex = ord(s2[r]) - ord('a')
            windowCount[rightIndex] += 1
            if windowCount[rightIndex] == s1Count[rightIndex]:
                matches += 1
            elif windowCount[rightIndex] == s1Count[rightIndex] + 1:
                matches -= 1
            
            # remove the left character
            leftIndex = ord(s2[l]) - ord('a')
            windowCount[leftIndex] -= 1
            if windowCount[leftIndex] == s1Count[leftIndex]:
                matches += 1
            elif windowCount[leftIndex] == s1Count[leftIndex] - 1 :
                matches -= 1
            l += 1
        
        return matches == 26
            




  
                


 
            