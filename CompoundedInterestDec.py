# Mihaela Bragagiu
#December 1 2024
#CIT-115 - Python
#Compound interest with Loops
#Calculate interest for each month in an account 



#####INPUTS
##Get valid original deposit
while True:
    try:
        fDeposit = float(input("What is the Original Deposit? (positive value): "))
        if fDeposit <=0:
            raise ValueError
    except ValueError:
        print("Deposit must be a positive numeric value.")
    else:
        break

##Get valid interest rate
while True:
    try:
        fInterestRate = float(input("What is the Interest Rate? (positive value): "))
        if fInterestRate <=0:
            raise ValueError
    except ValueError:
        print("Interest Rate must be a positive numeric value.")
    else:
        break

##Get valid number of months
while True:
    try:
        iMonths = int(input("What is the Number of Months?(positive value): "))
        if iMonths <=0:
            raise ValueError
    except ValueError:
        print("Number of Months must be a positive whole numeric value.")
    else:
        break

##Get valid goal value
while True:
    try:
        fGoal = float(input("What is the Goal Amount?(can enter 0 but not negative): "))
        if fGoal <0:
            raise ValueError
    except ValueError:
        print("Input Must be a positive numeric value.")
    else:
        break
#####END OF INPUTS


#######Convert interest rate to monthly rate
fMonthRate= fInterestRate/100 ##convert to decimal form
fMonthRate = fMonthRate/12 ##monthly interest rate

#######Compound interest loop to execute up to the number of months
iTemp=1 ##to count what month we're on in the loop
fAccountBalance = fDeposit ##Establish the current Account Balance
while(iTemp<=iMonths):
    fAccountBalance = fAccountBalance+ (fAccountBalance*fMonthRate)
    print("Month:  " + str(iTemp) + "  Account Balance is: " + f"${fAccountBalance:,.2f}")
    iTemp=iTemp+1

######Get the amount of months it will take to reach goals
iTemp=0 ##count the month it will take to reach goal
fTempBalance = fDeposit##make the TempBalance the Deposit so we start from month 1
while(fTempBalance <= fGoal):
    iTemp+=1
    fTempBalance =fTempBalance+ (fTempBalance*fMonthRate)
    if fTempBalance >=fGoal:
        print("It will take:  " + str(iTemp) + " months to reach the goal of " + f"${fGoal:,.2f}")

###END OF PROGRAM
