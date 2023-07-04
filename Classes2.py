class People:
    def __init__(self,name,age,gender):
        self.myname=name
        self.myage=age
        self.mygender=gender
    def show(self):
        print(self.myname,self.myage,self.mygender)
myobj=People("Scott Mcall" ,29 ,"Male")
myobj.show()
myobj=People("Lydia Martin" ,31 ,"Female")
myobj.show()
myobj=People("Cane Tehada" ,28 ,"Male")
myobj.show()