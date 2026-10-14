def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer:

# It will return: 3 4
# the for loop iterates through the list [1,2,3] so that if number in the list is more than 1 it adds 
#+1 and returns a number. So in practice it will be:
#1>1 --> false, so it will iterate further, 2>1 so it will add 1 and return 3(2+1=3), and 3>1 as well, so it will also add 1 and return 4.



# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer:
#the add_one(2) returns 3, since it adds to the value +1 and 2+1 becomes 3. Return gives a value back to the place in the code where it used the function
#the print only displays the result that was returned