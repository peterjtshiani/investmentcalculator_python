# Task 12 - Interest
# creating a calculator

import math

# getting the input from the user
P = float(input("Enter the deposit amount : "))
i = float(input("what is  your interest rate in percentage : "))
t = int(input("How long is your investment (number of years) : "))
interest = input("What type of interest are you interested in \"simple\" or \"compound\" interest? : ")

# calculating the interest rate in decimal
r = (i / 100)

# simple interest rate is calculated as follows:
SI = P*(1 + r * t)

# compound interest rate is calculated as follows:
CI = P* math.pow((1+r),t)


int1 = False
int2 = False

#displaying

if interest == "simple" :
    int1 = True

if interest == "compound" :
    int2 = True

# displaying

if int1 == True and int2 == False :
    print(SI)
    
elif int1 == False and int2 == True :
    print(CI)

else :
    while True :
        print("\nYou didn't choose any type of interest. Kindly try again. ")
        interest = input("\nWhat type of interest are you interested in \"simple\" or \"compound\" interest? : ")
        if interest == "simple" :
             print("R",SI)
             break
        if interest == "compound" :
            print("R",CI)
            break

        
print("\n*** The End ***")
