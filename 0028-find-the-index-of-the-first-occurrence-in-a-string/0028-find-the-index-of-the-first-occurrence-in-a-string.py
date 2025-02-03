class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is an empty string, return 0 (as per the definition)
        if not needle:
            return 0
        
        # Use find() to get the index of the first occurrence of needle in haystack
        return haystack.find(needle)
