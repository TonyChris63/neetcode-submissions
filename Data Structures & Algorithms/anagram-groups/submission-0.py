from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordkeys = {}
        for word in strs:
            # Sort the word to create a common key for anagrams
            sorted_word = ''.join(sorted(word))
            
            # Initialize the list for this key if it doesn't exist
            if sorted_word not in wordkeys:
                wordkeys[sorted_word] = []
            
            # Append the original word to the list for this sorted key
            wordkeys[sorted_word].append(word)
        
        # Return the grouped anagrams as a list of lists
        return list(wordkeys.values())
       