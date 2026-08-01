> HALF REVERSE

def if_palindrome(number):
    “””
	A number cannot be palindrome if it is negative or it ends with 0 and the number is not 0
    “””
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    # assign 0 to reverse_number 
    reverse_number = 0 
    
    # condition for stopping, given the reverse_number gets updated after every iteration
    while number>reverse_number:
        digit = number%10 # Find the last digit
        reverse_number = reverse_number *10 + digit # Formula to reverse the number 
        number = number // 10 # Remove the unit digit from the number
        # print(f"reverse number", reverse_number)
    
    # Condition to check whether the number is palindrome or not
    # For even case, number must be equal to the reverse_number 
    # For odd number case, remove the unit digit from the reverse_number and then check whether the number matches or not
    if number == reverse_number or number == reverse_number//10: 
	
        print("Given number is a palindrome.")
    else: 
        print("Given number is not a palindrome.")
    
    return number == reverse_number or number == reverse_number//10
    
if __name__ == "__main__" :
    number = 12921
    print(if_palindrome(number)) # Will give the result of the return statement in Boolean 
    
