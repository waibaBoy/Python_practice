def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)



print(is_anagram("listen", "silent"))
print(is_anagram("triangle", "integral"))
print(is_anagram("apple", "pale"))
print(is_anagram("Dormitory", "Dirty room"))
print(is_anagram("The Morse Code", "Here come dots"))
print(is_anagram("Astronomer", "Moon starer"))
