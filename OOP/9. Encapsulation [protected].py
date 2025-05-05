class School:
    def __init__(self):
        self.Name="Medford"
        self.Place="Bangalore"
        self._Revenue=400000 # Protected Member

class Faculty(School):
    pass

f1=Faculty()
print(f1._Revenue) # Accessing the protected member