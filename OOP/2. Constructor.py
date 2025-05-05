class Students:

    def __init__(self,Name,Roll_no,Dept):   # Constructor initialization
        self.Name=Name
        self.Roll_no=Roll_no
        self.Dept=Dept

    def display(self):
        print("Name =",self.Name)
        print("Roll no =",self.Roll_no)
        print("Dept =",self.Dept)

student1=Students("Alex",28,"Maths")
student1.display()