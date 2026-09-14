class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for char in s:
            if char.isalnum():
                new += char.lower()
        return new == new[::-1]
        
        # Reverse method
        # Create empty string
        # Loop through every char in the string
            # If the char is alphanumeric:
                # Add it into the empty string and make it lowercase
        # Compare the reverse string with original empty string


     