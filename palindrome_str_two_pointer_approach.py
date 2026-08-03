def is_palindrome(stra):
    left = 0
   
    right = len(stra)-1
    
    
    while right > left : 
        if stra[left]!= stra[right]:
           return False
        left += 1
        right -= 1
    return True
            
    
    
print(is_palindrome("abba"))
