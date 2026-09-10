class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for char in s:
            if char.isalnum():
                new += char
        return new.lower() == new[::-1].lower()
        # Create an empty string
        # Loop through the character in the string
            # If the character is alphanumeric then we add into the string
        # Then we reverse the string
        # Compare the reverse string (lowercase) with origianl string (lowercase)
