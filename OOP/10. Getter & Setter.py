class School:

    def __init__(self):
        self.__Name=None # Private Member


    def Set_Name(self,value):  # Setter Method
        self.__Name=value

    def Get_Name(self):     # Getter Method
        return self.__Name


s1=School()
s1.Set_Name("Willford")
print(s1.Get_Name())