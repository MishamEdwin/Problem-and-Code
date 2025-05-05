import backend
from tabulate import tabulate

class taxi_booker:
    def __init__(self):
       self.back=backend.backend()
       self.Database=[]

    def Book_Taxi(self,pickup,drop,ptime):
        available_taxi=None

        for taxi in self.back.Taxis:
            if not taxi.Booked: # to find an unbooked taxi
                available_taxi=taxi
                break
        if available_taxi:
            taxi_id=available_taxi.Taxi_ID
            available_taxi.Booked=True
            available_taxi.Current_location=drop
            distance = ord(drop) - ord(pickup)
            available_taxi.Free_time= ptime+distance
            available_taxi.Total_Earnings=available_taxi.Total_Earnings+(100+ (((distance*15)-5)*10)  )

            self.Database.append({
                'Taxi_ID':taxi_id,
                'Booking_ID':self.back.Booking_ID,
                'Customer_ID':self.back.Customer_ID,
                'Pickup_Location':pickup,
                'Drop_Location':drop,
                'Pickup_Time':ptime,
                'Drop_Time':available_taxi.Free_time,
                'Total_Earnings':available_taxi.Total_Earnings
            })

            self.back.Booking_ID+=1
            self.back.Customer_ID+=1

            print(f"Taxi {taxi_id} Booked Successfully!")
        else:
            print("No Taxis available at the moment!")



    def Display_Taxi_Details(self):
        for taxi in self.back.Taxis:
            print(f"Taxi : {taxi.Taxi_ID},"
                  f"Booked : {taxi.Booked}, "
                  f"Free Time : {taxi.Free_time}, "
                  f"Total Earnings : {taxi.Total_Earnings}, "
                  f"Current Location: {taxi.Current_location} ")
        print("____________________________________________________________________")

        if self.Database:
            for records in self.Database:
                for k,v in records.items():
                    print(k,":",v, end=" ")
                print()
            #print(tabulate(self.Database,headers="keys",tablefmt="pretty"))
        else:
            print("No Bookings Available")


















