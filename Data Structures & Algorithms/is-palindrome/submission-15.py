class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for char in s:
            if char.isalnum():
                new += char.lower()
        return new.lower() == new[::-1]
        # Create a new empty string
        # Loop through every char in the string
            # If the char is  alphanumeric
                # Add the char into the string
        # Compare the reverse string and the original string (make them lowercase)