
#! Scope: An area of a program where a namespace (variable/constant/function/etc.) that has a identified name can be 
#!        accessed/referenced to another part of the program.
#* Local Scope: When a namespace is defined in the a function.
#* Global Scope: When a namespace is defined outside of a function.


#! Global Scope example

character_intoxication = 10    #@ Being called from outside the function (Above the function is outside the scope of a function)

def dom_drink():
    tasty_beverage = 7
    print(f"{character_intoxication}\nOutside the function\n")

dom_drink()


#! Local Scope example

def drink_dom():
    beverage = 4            #@ Being called from inside the function 
    print(f"{beverage}\nInside the function\n")

drink_dom()


#! Is it a Prime Number code
#? Option 1
num = 73466


if num == 0 or num == 1:
    print("False")
elif num > 1:
    for i in range(2,num):
       if (num % i) == 0:
           print("False")
           break
    else:
       print("True")
       
else:
   print("False")

#? Option 2
def is_prime(num):
    if num == 0 or num == 1:
        print("False")
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print("False")
                break
        else:
            print("True")
    else:
        print("False")

is_prime(75)

#? Option 3, This option turns num into either true or false and can be called later 
def is_prime(num):
    
    if num == 2:
        return True
    if num == 1:
        return False    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
print("Is the number a prime number:", is_prime(73))

#! Modification of a Global Scope Variable