class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(numbers):
            temp = target - num
            if temp in dict:
                return [dict[temp]+1, index+1]
            dict[num] = index
        return []
        # Hashmap
        # Create an empty dictionary
        # Loop through the number in the numbers
            # target - number = temp
            # Chck whether the number is in the dictioanry or not
            # if yes: return answer
            # If no, put the number into the dictionary