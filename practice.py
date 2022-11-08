# Fizz Buzz revision before interviews


# Declare a variable with range from 1-100
# Iterate through 1-100
# If conditions for multiples for 3 and 5
# Also for both multiples of 3 and 5

numbers = range(100)
num = range(50)
def fizzbuzz(num):
    for i in num:
        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz")
        elif i % 3 == 0:
            print(f"Fizz")
        elif i % 5 == 0:
            print(f"Buzz")
        else:
            print(f"{i}")

fizzbuzz(numbers)
