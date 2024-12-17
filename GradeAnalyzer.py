# Mihaela Bragagiu
#November 24 2024
#CIT-115 - Python
#Grade Analyzer
#Takes 4 tests, and outputs average test score with optional lowest test dropped

##function used to test if the input grade is a number, and greater than 0

def testInput():
    #reusable function to test if inputted number is a float, and within the grade parameters
    fGrade = float(input())
    if fGrade>0:
        return fGrade
    else:
        #Output error if number too low or not a number
        print("Test scores must be greater than 0.")
        exit()


####CODE STARTS HERE

fAverageGrade=-10
strLetterGrade ='Z'
#asks for the inputs
strUserName = input("Name of person we are calculating grades for: ")

print("Test 1: ",end="")
fTest1 = testInput()
print("Test 2: ",end="")
fTest2 = testInput()
print("Test 3: ",end="")
fTest3 = testInput()
print("Test 4: ",end="")
fTest4 = testInput()


#Ask if they want to drop lowest grade
strDrop = input("Do you wish to drop the lowest grade Y or N?: ")
if strDrop== 'Y' or strDrop== 'y' or strDrop== "yes" or strDrop==  "Yes":
    #if the person wants to drop the lowest grade
    if fTest1<=fTest2 and fTest1<=fTest3 and fTest1<fTest4:
        #Test 1 is lowest therefore excluded
        fAverageGrade = (fTest2+fTest3+fTest4)/3
        
    elif fTest2<=fTest1 and fTest2<=fTest3 and fTest2<fTest4:
        #Test 2 is lowest therefore excluded
        fAverageGrade = (fTest1+fTest3+fTest4)/3
        
    elif fTest3<=fTest1 and fTest3<=fTest2 and fTest3<fTest4:
        #Test 3 is lowest therefore excluded
        fAverageGrade = (fTest1+fTest2+fTest4)/3
        
    elif fTest4<=fTest1 and fTest4<=fTest3 and fTest4<fTest2:
        #Test 4 is lowest therefore excluded
        fAverageGrade = (fTest1+fTest2+fTest3)/3
    else:
        print("Something went wrong with computing the average with a dropped grade.")
elif strDrop== 'N' or strDrop=='n' or strDrop== "no" or strDrop== "No":
    #if the person doesn't want to drop lowest grade
    fAverageGrade = (fTest1+fTest2+fTest3+fTest4)/4
else:
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()


##make sure to round the grade before assigning it a letter grade
##so the letter grade and outputted grade aren't possibly different
fAverageGrade = round(fAverageGrade, 1)

#section assigns letter grade
if fAverageGrade>=60:
    if fAverageGrade>=97.0:
        strLetterGrade = "A+"
    elif fAverageGrade>=94.0:
        strLetterGrade = 'A'
    elif fAverageGrade>=90.0:
        strLetterGrade = "A-"
    elif fAverageGrade>=87.0:
        strLetterGrade = "B+"
    elif fAverageGrade>=84.0:
        strLetterGrade = 'B'
    elif fAverageGrade>=80.0:
        strLetterGrade = "B-"
    elif fAverageGrade>=77.0:
        strLetterGrade = "C+"
    elif fAverageGrade>=74.0:
        strLetterGrade = 'C'
    elif fAverageGrade>=70.0:
        strLetterGrade = "C-"
    elif fAverageGrade>=67.0:
        strLetterGrade = "D+"
    elif fAverageGrade>=64.0:
        strLetterGrade = 'D'
    elif fAverageGrade>=60.0:
        strLetterGrade = "D-"
    else:
        print("Something went wrong with calculating the letter grade which was higher than an F.")
        exit()
elif fAverageGrade<60:
    strLetterGrade = 'F'
else:
    print("Something went wrong when computing the letter grade.")
    exit()


####OUTPUTS
print(strUserName + "'s Test average is: "+ str(fAverageGrade))
print("Letter Grade for the test is: " + str(strLetterGrade))
