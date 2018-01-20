print("Welcome to Fizz Buzz")
print("Please select a number to count too!")

restart = True
data = input()
while restart:
    try:
        val = int(data)
        n = val + 1
        game = True
        print("User selected {}! Let's start counting!" .format(n-1))
        while game:
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
            
            
            print("Would you like to try again? Select your new number or press x to exit!")
            
            
            if input() == "x":
                restart = False
                continue
            else:
                continue
    except ValueError:
        print("Cant use letters! Please choose a number, or hit x to exit")
        data = input()
        if data == "x":
            restart = False
        else:
            continue
if restart == False:
    print("Thank you for playing!")