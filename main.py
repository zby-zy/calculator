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
   
v1 = int(input("Enter your 1st number: "))
v2 = int(input("Enter your 2nd number: "))
c1 = Calc(v1, v2)    

print("Choose add(1), multiply(2), sub(3), divide(4)!")

selection = input("Select 1, 2 , 3 or 4: ")

if selection == "1":
    add_result = c1.add()
    print("Add: {}".format(add_result))

elif selection == "2":
    multiply_result = c1.multiply()
    print("Multiply: {}".format(multiply_result))

elif selection == "3":
    sub_result = c1.sub()   
    print("Sub: {}".format(sub_result))    
    
elif selection == "4":
    divide_result = c1.divide()
    print("Divide: {}".format(divide_result))
else:
    print("Error!")        
