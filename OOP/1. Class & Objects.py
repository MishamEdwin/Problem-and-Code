class Students:        # Class Definition
    Name=None          # Members Declaration
    Math_mark=None
    Physics_mark=None
    Chemistry_mark=None

    def cutoff(self):         # Function Declaration
        cutoff_mark=(self.Math_mark+self.Physics_mark+self.Chemistry_mark)/3
        return cutoff_mark


Student_1=Students()        #  Object Creation
Student_1.Name="Alex"
Student_1.Math_mark=75
Student_1.Physics_mark=83
Student_1.Chemistry_mark=93

Student_2=Students()
Student_2.Name="Brock"
Student_2.Math_mark=77
Student_2.Physics_mark=62
Student_2.Chemistry_mark=58

print(Student_2.cutoff()) # Function calling using object
