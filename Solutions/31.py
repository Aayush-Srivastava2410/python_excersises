class Calculator:
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2
    def add(self):
        return self.n1+self.n2
    def subtract(self):
        return self.n1-self.n2
    def multiply(self):
        return self.n1*self.n2
    def divide(self):
        return self.n1/self.n2

a=Calculator(12, 16).add()
s=Calculator(12, 16).subtract()
m=Calculator(12, 16).multiply()
d=Calculator(12, 16).divide()

print(a,s,m,d)