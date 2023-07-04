class Magari:
    def __init__(self,modelname,color,year,capacity):
        self.model=modelname
        self.mycolor=color
        self.myyear=year
        self.mycapacity=capacity
    def onyesha(self):
        print(self.model,self.mycolor,self.myyear,self.mycapacity)
        #Create an object
myobj=Magari("Mercedes" ,"Black" ,2022 ,"3000cc")
myobj.onyesha()
myobj=Magari("BMW" ,"Black" ,2021 ,"2500cc")
myobj.onyesha()