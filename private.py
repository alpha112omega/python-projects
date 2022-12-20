
class car:
    def __init__(self,name,model,price,per):
        self.name=name
        self.model=model
        self.price=price
        self.pr=per
    def __calc(self):
        return self.price + ((self.price*100)/self.pr)
    def data(self):
        return f"name= {self.name}\t model={self.model}\t price={self.__calc()}\t"

c= car("suzuki", "2021",2030 ,0.08)
print(c.data())
