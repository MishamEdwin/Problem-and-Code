class passenger():
    Id=None
    Name=None
    Age=None
    Berth_Preference=None
    Passenger_Id=None
    Alloted_Type=None
    Seat_number=None

    def __init__(self,Name,Age,Bert_Preference):
        self.Name=Name
        self.Age=Age
        self.Berth_Preference=Bert_Preference
        self.Passenger_Id= (self.Id+1)
        self.Alloted_Type=""
        self.Seat_number-=1






