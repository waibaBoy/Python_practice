def first_unique_char(s: str) -> int:
    """
    Returns the index of the first unique character in a string.
    If there are no unique characters, returns -1.
    """
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first unique character
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index
    
    return -1
print(first_unique_char("leetcode"))  # Output: 0
print(first_unique_char("loveleetcode"))  # Output: 2
print(first_unique_char("aabb"))  # Output: -1
print(first_unique_char("swiss"))  # Output: 2
print(first_unique_char("racecar"))  # Output: 0
