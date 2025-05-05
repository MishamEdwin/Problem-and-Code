class School:
    def __init__(self):
        self.Name="Rockford"
        self.Place="Chennai"
        self.__Revenue=5000000  # Private member

    def Display_revenue(self):
        print(self.__Revenue)

    def __Faculty_salary(self): # Private Method
        self.Salary=65000
        print(self.Salary)

    def Display_salary(self):    # Accessing the private method using public method
        self.__Faculty_salary()
s1=School()
s1.Display_revenue()
#print(s1._School__Revenue) #illegal move to access the private member
s1.Display_salary()