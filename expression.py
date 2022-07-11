class Expression :
    operatorPosition = 0
    operator = ""
    leftNumber = 0
    rightNumber = 0
    linesNeeded = 0

    def __init__(self, _item):
        self.fullExpression = _item
        self.operator = self.getOperator()
        self.leftNumber = self.getNumber("left")
        self.rightNumber = self.getNumber("right")


    def getOperator(self) :
        self.operatorPosition = self.getOperatorPosition()
        return self.fullExpression[self.operatorPosition]


    def getOperatorPosition(self) :
        possibleOperators = ["+", "-", "*", "/"]

        for operator in possibleOperators :
            if operator in self.fullExpression :
                if operator == "+" or operator == "-" :
                    return self.fullExpression.index(operator)
                else :
                    print("Error: Operator must be '+' or '-'")
                    quit()

        print("Error: Unusable operator in item " + self.fullExpression + ".")
        quit()


    def getNumber(self, position) :
        if position == "left" :
            number = self.fullExpression[:self.operatorPosition]
        else :
            number = self.fullExpression[self.operatorPosition + 1:]

        number = number.replace(" ", "")
        numberLength = len(number)

        try :
            number = int(number)
        except : 
            print("Error in item " + self.fullExpression + ". There must be only numbers and operators in the expression.")
            quit()

        if numberLength > 4 :
            print("Error in item " + self.fullExpression + ". Numbers cannot be more than four digits long.")

        return number

    def longestOperand(self) :
        if self.leftNumber > self.rightNumber :
            return self.leftNumber
        else :
            return self.rightNumber
    

    def result(self) :
        switcher = {
            "+": self.leftNumber + self.rightNumber,
            "-": self.leftNumber - self.rightNumber
        }

        return switcher.get(self.operator, 0)





