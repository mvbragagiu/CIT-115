# Mihaela Bragagiu
#November 10 2024
#CIT-115 - Python
#Compound Interest

#input prompts
fPrincipal = float(input("Enter the starting Principal: "))
fAnnualInterest = float(input("Enter the annual interest rate: "))
iInterestCompound = int(input("How many times per year is the interest compounded? "))
iYears = int(input("How many years will the account earn interest? "))

#calculations

fFutureValue = float(fPrincipal *((1+((fAnnualInterest/100)/iInterestCompound))**(iInterestCompound*iYears)))


#output

print("At the end of ", iYears, "years you will have $","{:.2f}".format(fFutureValue))
