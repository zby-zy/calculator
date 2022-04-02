class Calc(object):
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b
        
    def add(self):
        return self.value1+self.value2
    
    def multiply(self):
        return self.value1*self.value2
    
    def sub(self):
        return self.value1-self.value2
    
    def divide(self):
        return self.value1/self.value2
    
print("Select operation.\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

v1 = int(input("Enter your 1st number: "))
v2 = int(input("Enter your 2nd number: "))
c1 = Calc(v1, v2)    

selection = input("Select 1, 2 , 3 or 4: ")

if selection == "1":
    add_result = c1.add()
    print("Addition: {}".format(add_result))

elif selection == "2":
    multiply_result = c1.multiply()
    print("Multiplication: {}".format(multiply_result))

elif selection == "3":
    sub_result = c1.sub()   
    print("Subtraction: {}".format(sub_result))    
    
elif selection == "4":
    divide_result = c1.divide()
    print("Division: {}".format(divide_result))
    
else:
    print("Error!")        
