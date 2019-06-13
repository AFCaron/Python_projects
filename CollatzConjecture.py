#Collatz Conjecture - 
#Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
#If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1



#picking a number, could have been thru an random int generation
num = int(input("please select a number > 1 "))
#initializing the step variable
step = 0

#as long as num > 1 the program runs
while num != 1:
    #case for even number
    if num%2 == 0 and num > 1:
        num = num / 2
        step = step + 1
    
    #case for odd number
    elif num % 2 != 0 and num > 1:
        num = num*3 + 1
        step = step + 1
   
    #case when num = 1
    elif num == 1:
        break

print(f"the number of step is {step}")
