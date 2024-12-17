#Mihaela Bragagiu
#December 14 2024
#CIT-115 - Python
#Real estate analyzer
#User enters property sales and gets the min, max, average, median, total, and commission prices.


#greeting
print("Welcome to the Sales Analyzer v1.0 by Mihaela Bragagiu.")


######get a string as input, and returns a float that is positive and non-zero
def getFloatInput(sTempString):
    while True:
        try:
            fNum = float(input(sTempString))
            if fNum <=0:
                raise ValueError
            return fNum
        except ValueError:
            print("Please enter a valid number that is positive and higher than zero.")
        else:
            break
    return fNum


######Gets the median of the list, the list is sorted already when you get it
def getMedian(lTempList):

    iCountList = len(lTempList)#Get amount of entries
    
    if iCountList % 2 == 0:##Means it's even.
        fMedian = ((lTempList[int(iCountList/2)])+(lTempList[int((iCountList/2)-1)]))/2
    else:##Means it's odd
        fMedian = lTempList[int(iCountList/2)]
    return fMedian
#######



####Print the list correctly

def printList(lTempList):
    iCountList = len(lTempList)
    iCounter =0
    while iCounter<iCountList:
        print("Property "+str(iCounter+1)+ "   $ "+"{:,.2f}".format(lTempList[iCounter]))
        iCounter=iCounter+1
    return
########




#################
#
#
#
#
#
#################MAIN CODE STARTS HERE

def main():
    fInput =0
    sStopOrGo = '0'
    lSalesPrices= []

    #Loop to get input list
    while sStopOrGo!="N" or sStopOrGo!="n" :

        fInput = getFloatInput("Please enter a sales price: ")
        lSalesPrices.append(fInput)
        ##loop to make sure valid Y or N was put
        while True:
            try:
                sStopOrGo = input("Enter another value Y or N?: ")
                if sStopOrGo != 'N' and sStopOrGo != 'n' and sStopOrGo != 'Y' and sStopOrGo != 'y':
                    raise ValueError
            except ValueError:
                print("Please only enter Y or N")
            else:
                break
        if sStopOrGo == 'N' or sStopOrGo == 'n':
            break
    ####end of loop


    


    ##Sort the list

    lSalesPrices.sort()#sort ascending

    #
    #
    #
    #
    #
    ###### PRINTING EVERYTHING
    printList(lSalesPrices)
    print("Minimum   :       " + "$ "+"{:,.2f}".format(lSalesPrices[0]))#it's sorted already so the first should be the lowest]
    print("Maximum   :       " + "$ "+"{:,.2f}".format(lSalesPrices[-1]))
    print("Total     :       " + "$ "+"{:,.2f}".format(sum(lSalesPrices)))
    print("Average   :       " + "$ "+"{:,.2f}".format(sum(lSalesPrices)/len(lSalesPrices))) 
    print("Median    :       " + "$ "+"{:,.2f}".format((getMedian(lSalesPrices))))
    print("Commission:       " + "$ "+"{:,.2f}".format((sum(lSalesPrices))*0.03))
        


    
    return
############################

#call main code
main()
