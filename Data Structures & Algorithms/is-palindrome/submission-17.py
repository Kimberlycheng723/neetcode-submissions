class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for char in s:
            if char.isalnum():
                new += char
        return new.lower() == new[::-1].lower()
        # Create an empty new string
        # Loop through character in the array
            # If the character is alphanum
                # Add into the new string
        # Compare the reverse new string and original new string
     