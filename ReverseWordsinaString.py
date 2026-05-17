# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # strip the trailing or leading spaces
        words = s.split() # split the string
        left, right = 0, len(words)-1
        print(words)

        while left<right:
            
            words[left],words[right] = words[right],words[left]
            left += 1
            right -=1
        return " ".join(words)
        
       
