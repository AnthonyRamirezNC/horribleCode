class Calculator:
    # funciton to add numbers
    def add(num1, num2):
        #return the numbers added
        return num1 + num2
    
    #function to multiply numbsers
    def multiply(num1, num2):
        #return the numbers multiplied
        return num1 * num2

    #function to divide numbers
    def divide(num1, num2):
        #return the quotient of the numbers
        return num1 / num2

    #function to subtract second number from first number
    def subtract(num1, num2):
        #return the numbers subtracted
        return num1 - num2

calc = Calculator
print(calc.add(1,4))
print(calc.subtract(4,1))
print(calc.multiply(6,4))
print(calc.divide(100,4))
    
