import passenger

class ticket_booker(passenger):
    # Total 63 Berths(21U + 21M + 21L) + 18 RAC + 10 WL
    available_lower_berths=21
    available_middle_berths=21
    available_upper_berths=21
    available_rac=18
    available_waiting_list=10

    booked_ticket_list=[] #list of berth passengers
    rac_list=[]
    waiting_list=[]

    lower_berth_positions=list(range(1,22)) # [1 to 21]
    middle_berth_positions=list(range(1,22)) # [1 to 21]
    upper_berth_positions=list(range(1,22)) # [1 to 21]
    rac_positions=list(range(1,19)) #[1 to 18]
    waiting_list_positions=list(range(1,11)) #[1 to 10]

    passengers={} # Map of Id and Passengers

    def book_ticket(self,passenger,berth_info,alloted_berth):
        passenger.Seat_number=berth_info
        passenger.Alloted_Type=alloted_berth

        # add passenger to the map
        self.passengers[passenger.Passenger_Id]=passenger

        # add passenger_id to the booked ticket
        self.booked_ticket_list.append(passenger.Passenger_Id)

        print("-------------------Booked Successfully----------")
