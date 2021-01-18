#############################################
## Name: Aleck Bowen Sun                   ##
##                                         ##
## Program: Addition and multiplication    ##
##          command line calculator        ##
##                                         ##
## Date: January 15, 2021                  ##
#############################################

import sys

def main():
    #Makes sure only one argument is passed
    assert len(sys.argv) == 2, (
        "Invalid input -- expected 1 string argument got: " + str(len(sys.argv)-1)) 
    inputs = sys.argv[1]

    #Calculation
    print(addMultiply(inputs))

def addMultiply(inputs):
    #Base case: Number only or empty
    if len(inputs) == 0 or inputs[0] != "(":
        return int(inputs)

    else:
        #Gets operator and index where first parameter begins
        parameterStart = inputs.find(" ") + 1
        operator = inputs[1:parameterStart-1]

        #If first parameter is not nested
        if inputs[parameterStart] != "(":
            #second parameter starts at first space index
            parameter2Start = inputs.find(" ", parameterStart+1)

            #Sets parameters based on where second and first parameter index begin
            parameter1 = inputs[parameterStart:parameter2Start]
            parameter2 = inputs[parameter2Start+1:len(inputs)-1]

        else:
            #second parameter starts when first parameter ends
            parameter2Start = inputs.index(") ")

            parameter1 = inputs[parameterStart:parameter2Start+1]
            parameter2 = inputs[parameter2Start+2:len(inputs)-1]

        #Arithmetic based on operator
        if (operator == "multiply"):
            return addMultiply(parameter1) * addMultiply(parameter2)
        
        elif (operator == "add"):
            return addMultiply(parameter1) + addMultiply(parameter2)

        else:
            return "Invalid operator"
        
main()
