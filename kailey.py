import pandas as pd
import numpy as np

dictionary = {}
dictionary["Kaily"] = "Fucking Hot"
print(dictionary)
dictionary["Kaily"] = int(0)
print(dictionary)
dictionary["Kaily"] += 10
dictionary["Madison"] = 7

values = dictionary.values()
for value in values:
    print(value)

print(max(values))

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        print("k is:", k)
        print("s(str) is:", s)
        
        start_window = 0
        end_window = 0
        
        dictionary = {}
        char_frequency = 0
        max_length = 0
        while end_window
        

s = "ABABBBA"
k = 3
solution = Solution()
solution.characterReplacement(s,k)

