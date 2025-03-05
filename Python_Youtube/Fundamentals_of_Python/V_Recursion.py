# ========== Recursion ==========

print( "Recursion Summary")

## ======= Recursion Overview =========
    # Common way to explain recursion is by using factorials 

# 3! = 3 x 2 x 1 = 6
# 4! = 4 x 3 x 2 x 1 = 24
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# Now define the function to produce the results above to calc factorial of any number: 

def factorial(n):
    if n == 1:                          # Always need to define a base case for factorial
        return 1                            # We know 1! will return 1 hence if n == 1 is True function will return 1
                                            # Always need to have a base case to ensure the recursion stops
                                            # otherwise at 1000 calls we'll get a recursion error where python at default haults this at 1000
    return n*factorial(n-1)             # If n != 1 then we move onto the recursive case as we have here
                                            # E.g if n == 2 return is 2*((2-1)!) which is 2
                                            # E.g if n == 3 return 3*((3-1)!) which is 6
                                            # E.g if n == 4 returns 4((4-1)) which is 4x 3! which is 2

print(factorial(3))                     # Returns 6
print(factorial(4))                     # Returns 24
print(factorial(5))                     # Returns 120