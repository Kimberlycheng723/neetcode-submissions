class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a empty default dictionary in list
        dict = defaultdict(list)

        # Loop through each of the word in the strs
        for word in strs:
            sortedWord = ' '.join(sorted(word))
            dict[sortedWord].append(word) 
            # sort the word (remember sort will become char)
            # Put the item into dict {sortedWord: word}
        
        # Return the dictionary values in list
        return list(dict.values())