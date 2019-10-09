num = int(input("Enter a number between 1  and 100 : "))
for x in range(num):
    x = x+1
    if ((x % 3 == 0) and (x % 5 == 0)):
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)
