# Mihaela Bragagiu
#November 17 2024
#CIT-115 - Python
#Temperature Coverter - convert C to F and F to C


#greeting
print("Welcome to the TemperatureConverter v1.0 by Mihaela Bragagiu.")


#inputs
fTempInput = input("Enter a temperature: ")

#if loops start
if float(fTempInput):
    sFahorCel = input("Is the temp F for Fahrenheit or C for Celsius?: ")
    #converts to float
    fTempInput = float(fTempInput)

    ########
        #checks if its Fahrenheit
    if sFahorCel=='F' or sFahorCel=='f':
        #if temperature if Fahrenheit
        if fTempInput<212 and fTempInput>-460:
            fCalcTemp= (5.0 / 9) * (fTempInput-32)
            print("The Celsius equivilent is "+"{:.1f}".format(fCalcTemp)+ "C")
        #if temp isn't possible
        else:
            print("Fahrenheit temperatures cannot be higher than 212 and lower than -460.")

    ########
        #checks if its Celsius
    elif sFahorCel=='C' or sFahorCel=='c':
        if fTempInput<100 and fTempInput>-273.15:
            fCalcTemp= (((9.0 / 5.0) * fTempInput)+ 32)
            print("The Fahrenheit equivilent is "+"{:.1f}".format(fCalcTemp) + "F")

            #if temp isn't possible
        else:
            print("Fahrenheit temperatures cannot be higher than 100 and lower than -273.15.")

    ######## 
        #if it isn't F or C
    else:
        print("Please enter only C or F to define the temperature.")

#if number input wasn't numeric
else:
    print("Please enter only numbers for the temperature.")


#ending prints
print("")
print("Thank you for using the Temperature Converter v1.0.")
