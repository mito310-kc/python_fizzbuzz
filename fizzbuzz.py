print("Fizz Buzz start!!!!")
def fizz_buzz(i):
    print(i)   
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3==0:
        print("Fizz")
    elif i % 5==0:
        print("Buzz")
for i in range(1,101):
    fizz_buzz(i)

