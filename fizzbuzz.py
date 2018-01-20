n = 35
game = True

print("Fizz Buzz is counting up to {}" .format(n))

while game:
    n = int(n) + 1 
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