def is_palindrome(number):

	forward = str(number)
	backward = str(n)[::-1]

    if forward == backward
        return True
        
    else:
        return False
        
        
def is_prime(number)
    
    if number < 2:
        return False
        
    for i in range(2, number):
        
        if number % i == 0:
            return False
            
    return True
    

def is_prime_palindrome(number)

    if number < 0:
        return False
        
    palindrome = is_palindrome(number)
    prime = is_prime(number)
    
    if palindrome == True and prime == True
        return True
    else:
        return False

    