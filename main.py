# Declare a variable with range from 1-100
# Iterate through 1-100
# If conditions for multiples for 3 and 5
# Also for both multiples of 3 and 5

Numbers = range(100)
Num = range(30)
def FizzBuzz(num):
    for i in num:
        if i % 3 == 0 and i % 5 == 0:
            string()
        elif i % 3 == 0:
            print (f"Fizz {i}")
        elif i % 5 == 0:
            print (f"Buzz {i}")
        else:
            print (i)
    

def string():
    print ("FizzBuzz")



FizzBuzz(Numbers)
