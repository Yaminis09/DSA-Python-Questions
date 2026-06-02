
def pp(str_a):
    left = 0
    right = len(str_a)-1
    while left<right:
        if str_a[left] != str_a[right]:
            return "not palindrome"
       
        left+=1
        right -=1
    return "its a palindrome"
a = pp(str_a)
print(a)
