import sys
class process_derivative:
    def __init__(self, input):
        self.input = input
        self.splitted = self.splitting_strings(input)

    def splitting_strings(self,input):  # a function that returns a list containing a list containing constant,variable,and power
        polynom = input.replace("-", "+-")  # replacing - to +- so easier to split
        NumberList = polynom.split("+")  # splitting it into a list
        variable = ""
        if "" in NumberList:
            NumberList.remove("")
        splitted = []  # a list containing a list containing constant,variable,and power
        for element in NumberList:
            splitElement = element.split("*")
            if len(splitElement) == 1:  # if it's constant but no variable or variable with no constant
                try:  # if it's constant with no variable
                    int(splitElement[0])
                    splitElement.append("^0")
                except:  # if it's variable with 1 or -1 as constant
                    if "-" in splitElement[0]:  # if it's variable with -1 as constant
                        splitElement[0] = splitElement[0].replace("-", "")  # removing the - in variable
                        splitElement.insert(0, "-1")  # adding -1 as constant
                    else:
                        splitElement.insert(0, "1")  # if it's variable with 1 as constant

            splitPower = splitElement[1].split("^")
            if len(splitPower) == 1:  # if variable^1
                splitElement[1] = splitPower[0]  # adding to split element
                splitElement.append("1")  # adding power as 1
                if variable == "":  # if variables are same
                    variable = splitPower[0]
                else:
                    if variable != splitPower[0]:
                        print("invalid input")
                        sys.exit(None)#exit if it's different variable
            else:
                splitElement[1] = splitPower[0]
                splitElement.append(splitPower[1])
                if variable == "":  # checking if variables are same
                    variable = splitPower[0]
                else:
                    if variable != splitPower[0] and splitPower[0] != "":
                        print("invalid input")
                        sys.exit(None)#exit if it's different variable
            splitted.append(splitElement)
        for element in splitted:  # a function that defines the variable
            if element[1] == "":
                element[1] = variable
        return splitted

    def get_first_derivative(self):  # a function that gives the derivative and connect the splitting_strings with formatting_first
        splitted = self.splitted
        derivative = self.formatting_first(splitted)
        return derivative

    def formatting_first(self, splitted):  # a function to format the splitted
        result = ""#an empty string that will be added
        start = True
        for zero_splitted in splitted:
            zero_splitted[0] = int(zero_splitted[0])  # old constant
            zero_splitted[2] = int(zero_splitted[2])  # old power
            new_constant = zero_splitted[0] * zero_splitted[2]  # new constant
            new_power = zero_splitted[2] - 1  # new power
            new_variable = zero_splitted[1]
            if new_constant != 0:
                if new_constant < 0:  # printing for minus
                    result = result + str(new_constant)#printing the next constant
                    if new_power != 0:#if not variable^0 then print this
                        result = result + "*" + str(new_variable)#printing the variable
                        if new_power != 1:  # if variable not variable^1 then print this
                            result = result + "^" + str(new_power)#printing the power
                else:  # printing for plus
                    if start:
                        result = result + str(new_constant)
                    else:
                        result = result + "+" + str(new_constant)
                    if new_power != 0:
                        result = result + "*" + str(new_variable)
                        if new_power != 1:
                            result = result + "^" + str(new_power)
            else:
                if len(splitted) == 1:#only print 0 if the constant is zero
                    result += "0"
            start = False
        return result