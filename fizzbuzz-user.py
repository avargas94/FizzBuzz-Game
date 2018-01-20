print("Welcome to Fizz Buzz")
print("Please select a number to count too!")

game = True

val = input()

def isNumber(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

while game:
    
    if isNumber(val) == True:
        
        n = int(val) + 1
        
        print("User selected {}! Let's start counting!" .format(n-1))
       
        for n in range(1,n):
            if (n % 3 == 0) and (n % 5 == 0):
                print("Fizz Buzz")
                n += 1
            elif n % 3 == 0:
                print("Fizz")
                n += 1
            elif n % 5 == 0:
                print("Buzz")
                n += 1
            else:
                print(n)
                n += 1
        game = False
    else:
        print("Please make sure that you are choosing a number!")
        val = input()
    
if game == False:
    print("Thank you for playing")
    
    

