class Taxi:
   def __init__(self,taxi_id):
      self.Taxi_ID = taxi_id
      self.Booked=False
      self.Free_time=6
      self.Total_Earnings=0
      self.Current_location="A"


class backend:

    def __init__(self):
       self.Booking_ID = 1
       self.Customer_ID = 1  # booking id and customer id are treated same
       self.Taxi_Count = 4
       self.Taxis=[Taxi(i+1) for i in range(self.Taxi_Count)] # Taxi objects
       self.Current_Time = None





