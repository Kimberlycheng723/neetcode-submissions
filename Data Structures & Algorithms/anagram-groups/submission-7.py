class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create an empty default dict in list
        dict = defaultdict(list)

        for word in strs:
            table = [0]*26
            for char in word:
                table[ord(char) - ord('a')] += 1
            dict[tuple(table)].append(word)
        
        return list(dict.values())
        
      
        