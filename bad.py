class Calcualtor:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    # funciton to add numbers KISS
    def adding_numbers(num1,num2):
        #using a stack because it is OPTIMALLLLLL
        stack = []
        addition = 0  
        stack.append(num1)
        stack.append(num2)

        for i in stack:
             addition += i
        return addition
        
    
    #def Mutliplying 


calc = Calcualtor
print(calc.adding_numbers(1,4))
    
