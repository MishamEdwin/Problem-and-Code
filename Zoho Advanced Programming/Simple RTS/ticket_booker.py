import backend
class ticket_booker():
    def __init__(self):
        self.tickets=[]
        self.bk = backend.backend  # object of the backend class

    def Book_Ticket(self,Name,Age,Berth_Preference):
        ticket_id=self.bk.Id
        self.bk.Id+=1

        if self.bk.Upper>0 or self.bk.Lower>0 or self.bk.Middle>0:
            if (Berth_Preference[0] == 'U' or Berth_Preference[0] == 'u'):
                self.bk.Upper -= 1

            if (Berth_Preference[0] == 'L' or Berth_Preference[0] == 'l'):
                self.bk.Lower -= 1

            if (Berth_Preference[0] == 'M' or Berth_Preference[0] == 'm'):
                self.bk.Middle -= 1

            self.tickets.append({'ID': ticket_id, 'Name': Name, 'Age': Age, 'Berth_Preference': Berth_Preference})
            print(f"Ticket Booked! Ticket ID:{ticket_id}")
            self.bk.update_available_tickets()
            return

        elif self.bk.RAC>0:
            Berth_Preference="RAC"
            self.tickets.append({'ID': ticket_id, 'Name': Name, 'Age': Age, 'Berth_Preference': Berth_Preference})
            print(f"Ticket Booked in RAC Ticket ID:{ticket_id}")
            self.bk.RAC -=1
            self.bk.update_available_tickets()
            return

        elif self.bk.Waiting_list>0:
            Berth_Preference = "Waiting_List"
            self.tickets.append({'ID': ticket_id, 'Name': Name, 'Age': Age, 'Berth_Preference': Berth_Preference})
            print(f"You are in Waiting List! Ticket ID:{ticket_id}")
            self.bk.Waiting_list -= 1
            self.bk.update_available_tickets()
            return


    def Cancel_Ticket(self,Id):
        ticket_id=Id
        for ticket in self.tickets:
            if ticket['ID']==ticket_id:
                self.tickets.remove(ticket)
                print(f"Ticket{ticket_id} has been canceled successfully")
                backend.backend.Id-=1
                self.bk.update_available_tickets()
                return
        print(f"Ticket ID :{ticket_id} not found")


    def Display_Booked_Tickets(self):
        for ticket in self.tickets:
              print(f"Id:{ticket['ID']}, Name:{ticket['Name']}, Age:{ticket['Age']}, Berth: {ticket['Berth_Preference']}")
              #print(ticket['ID'],ticket['Name'],ticket['Age'])

    def Display_Available_Tickets(self):
        print(f"Avaliable Tickets : {self.bk.Available_Tickets} "
              f"\nUpper Berth : {self.bk.Upper}"
              f"\nLower Berth : {self.bk.Lower}"
              f"\nMiddle Berth : {self.bk.Middle}"
              f"\nRAC : {self.bk.RAC}"
              f"\nWaiting List : {self.bk.Waiting_list} ")