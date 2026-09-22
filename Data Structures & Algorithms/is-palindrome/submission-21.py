class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower()
        return newStr == newStr[::-1]
        # Initiate an empty new string
        # Loop through the char in the s:
            # Check whether if it is alphanumeric
                # Add into the new string
        # Compare the original string with the reverse string
     