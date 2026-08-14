class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            table = [0]*26
            for char in word:
                table[ord(char) - ord('a')] += 1
            res[tuple(table)].append(word) 

        return list(res.values())
       # Create a defaultdict in list
       # loop through each word in the strs
            # Loop through each character in the word
                # Count the ord and put into the dict {0010112 = 'act'}

                # Return the res(values) in list
        
  