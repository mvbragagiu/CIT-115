#Mihaela Bragagiu
#December 07 2024
#CIT-115 - Python
#Paint Job with Function and Outputs
#Gives you the total cost for a paintjob and puts outputs in a textfile

#################IMPORTS
import math

#################FUNCTIONS

######Gets a number from input, makes sure it's accurate and prints any and all errors to file
def getFloatInput(sText):
    while True:
        try:
            fNum = float(input(sText))
            if fNum <=0:
                raise ValueError
            return fNum
        except ValueError:
            print("Please enter a valid Number.")
        else:
            break
######get the total gallons of paint
def getGallonsOfPaint(fSquareFeetWall,fFeetGallon):
    iTotalGallons = math.ceil(fSquareFeetWall/fFeetGallon)
    return iTotalGallons

######get total labor hours
def getLaborHours(fLaborHoursPerGallon,iTotalGallons):
    fTotalLaborHours = fLaborHoursPerGallon*iTotalGallons
    return fTotalLaborHours
######get total labor cost
def getLaborCost(fTotalLaborHours,fLaborCharge):
    fTotalLaborCost = fTotalLaborHours*fLaborCharge
    return fTotalLaborCost

######get total labor cost
def getPaintCost(iTotalGallons,fPaintPrice):
    fTotalPaintCost = iTotalGallons*fPaintPrice
    return fTotalPaintCost

######get sales tax based on state
def getSalesTax(sState):
    if sState == 'CT':
        return 0.06
    elif sState == 'MA':
        return 0.0625
    elif sState == 'ME':
        return 0.085
    elif sState == 'RI':
        return 0.07
    elif sState == 'VT':
        return 0.06
    else: ##This includes NH because the tax rate is 0 there
        return 0


def getTotalTax(fSalesTaxRate,fTotalLaborCost,fTotalPaintCost):
    return ((fTotalLaborCost+fTotalPaintCost)*fSalesTaxRate)


#######Show Cost Estimate and use both_input to input to file and terminal
def showCostEstimate(sLastName,iTotalGallons,fTotalLaborHours,fTotalLaborCost,fTotalPaintCost,fTotalTax,fTotalCost):

    ######local function to print to terminal and file at the same time with value
    def print_both(sText,vValue):
        sPrintThis= str(sText + "{:,.2f}".format(vValue))
        print(sPrintThis)
        print(sPrintThis,file=f)#Gives output and puts it in file
        
    sFileName = sLastName+".txt"
    with open(sFileName,"w") as f:
        print_both("Gallons of paint:  ",iTotalGallons)
        print_both("Hours of labor:    ",fTotalLaborHours)
        print_both("Paint charges:    $",fTotalPaintCost)
        print_both("Labor charges:    $",fTotalLaborCost)
        print_both("Tax:              $",fTotalTax)
        print_both("Total cost:       $",fTotalCost)
        
    print(sFileName + " was created!")
        
    

#################
#
#
#
#
#
#################MAIN CODE STARTS HERE

def main():
    ##Get all the inputs
    fSquareFeetWall = getFloatInput("Enter wall space in square feet:  ")
    fPaintPrice = getFloatInput("Enter paint price per gallon:  ")
    fFeetGallon = getFloatInput("Enter feet per gallon:  ")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon:  ")
    fLaborCharge = getFloatInput("Labor charge per hour:  ")
    sState = input("State job is in:  ")
    sLastName = input("Customer Last Name:  ")

    ##functions to get variables
    iTotalGallons = getGallonsOfPaint(fSquareFeetWall,fFeetGallon)
    fTotalLaborHours = getLaborHours(fLaborHoursPerGallon,iTotalGallons)
    fTotalLaborCost = getLaborCost(fTotalLaborHours,fLaborCharge)
    fTotalPaintCost = getPaintCost(iTotalGallons,fPaintPrice)
    fSalesTaxRate = getSalesTax(sState)
    fTotalTax = getTotalTax(fSalesTaxRate,fTotalLaborCost,fTotalPaintCost)
    fTotalCost =fTotalPaintCost+fTotalLaborCost+fTotalTax
    
    ##calls show Cost Estimate
    showCostEstimate(sLastName,iTotalGallons,fTotalLaborHours,fTotalLaborCost,fTotalPaintCost,fTotalTax,fTotalCost)
    return
############################

#call main code
main()
