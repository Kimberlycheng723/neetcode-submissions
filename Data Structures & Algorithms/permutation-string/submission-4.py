class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, windowCount = [0]*26, [0]*26
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
            # add the character from the right into window
            rightIndex = ord(s2[r]) - ord('a')
            windowCount[rightIndex] += 1
            if s1Count[rightIndex] == windowCount[rightIndex]:
                matches += 1
            elif s1Count[rightIndex]+1 == windowCount[rightIndex]:
                matches -= 1

            # remove the character from the left into window
            leftIndex = ord(s2[l]) - ord('a')
            windowCount[leftIndex] -= 1
            if s1Count[leftIndex] == windowCount[leftIndex]:
                matches += 1
            elif s1Count[leftIndex]-1 == windowCount[leftIndex]:
                matches -= 1
            l += 1
        return matches == 26





                
 
            