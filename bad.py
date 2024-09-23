class Calcualtor:
    # funciton to add numbers 
    # violates KISS principle
    def adding_numbers(num1, num2):
        #using a stack because it is OPTIMALLLLLL
        stack = []
        addition = 0  
        stack.append(num1)
        stack.append(num2)

        for i in stack:
             addition += i
        return addition
    
    #function to multiply numbers
    #violats seperation of concerns principle
    def multiply(num1, num2):
        total = 0
        for i in range(num2):
            total = Calcualtor.adding_numbers(total, num1)

        return total

    #function to divide numbers
    #violates smelly comments principle
    def d(a, b):
        #initialize c to keep return total
        c=0
        #set return value to quotient of two inputs
        c = a / b
        #return return value
        return c
    #violates YAGNI
    #function to add 1 to the passed number
    def addOne(num1):
        #Anthony definitley made this stupid function. Does he even know how to center a div? 
        return num1 + 2 - 1



calc = Calcualtor
print(calc.adding_numbers(1,4))
#print(calc.subtraction(4,1))
print(calc.multiply(6,4))
print(calc.d(100,4))
print(calc.addOne(100))

    
