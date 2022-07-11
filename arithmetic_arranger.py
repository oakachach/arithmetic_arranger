from expression import Expression

def arithmetic_arranger(expressionList, showAnswers = False) :
    operations = list()
    
    if len(expressionList) > 5 :
        print("Error: Too many problems.")
        quit()
    
    for item in expressionList :
        expression = Expression(item) 
        operations.append(expression)
    
    printLeftSideNumbers(operations)
    printRightSideNumbers(operations)
    printLines(operations)
    if showAnswers == True :
        printResult(operations)


def printLeftSideNumbers(_operations) :
    whiteSpace = ''
    counter = 0
    for operation in _operations : 
        counter += 1
        if len(str(operation.leftNumber)) < (len(str(operation.rightNumber)) + 2) :
            whiteSpaceNeeded = (len(str(operation.rightNumber)) + 2) - len(str(operation.leftNumber))
            for i in range(0, whiteSpaceNeeded) :
                whiteSpace = whiteSpace + " "
        
        if counter != len(_operations) : 
            print(whiteSpace + str(operation.leftNumber) + " ", end = " ")
        else :
            print(whiteSpace + str(operation.leftNumber) + " ")
        operation.linesNeeded = len(whiteSpace) + len(str(operation.leftNumber))
        whiteSpace = ""
        

def printRightSideNumbers(_operations) :
    whiteSpace = ''
    counter = 0
    for operation in _operations :
        counter += 1
        if (len(str(operation.rightNumber)) + 2) < len(str(operation.leftNumber)) :
            whiteSpaceNeeded = len(str(operation.leftNumber)) - (len(str(operation.rightNumber)) + 2)

            for i in range(0, whiteSpaceNeeded) :
                whiteSpace = whiteSpace + " "

        if counter != len(_operations) :
            print(operation.operator, str(operation.rightNumber) + " ", sep = " " + whiteSpace, end = " ")
        else :
            print(operation.operator, str(operation.rightNumber) + " ", sep = " " + whiteSpace)
        whiteSpace = ""


def printLines(_operations) :
    line = ""
    counter = 0
    for operation in _operations :
        counter += 1
        for i in range(0, operation.linesNeeded) :
            line += "-"
        
        if counter != len(_operations) :
            print(line, end = "  ")
        else :
            print(line)
        line = ""


def printResult(_operations) :
    whiteSpace = ""
    whiteSpaceNeeded = 0
    for operation in _operations :
        whiteSpaceNeeded = operation.linesNeeded - len(str(operation.result()))
        for i in range(0, whiteSpaceNeeded) :
            whiteSpace += " "

        print(whiteSpace + str(operation.result()), end = "  ")
        whiteSpace = ""
        