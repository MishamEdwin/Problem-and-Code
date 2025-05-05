import backend
import ticket_booker

if __name__=="__main__":
    #obj =  file name   . class name
    tb=ticket_booker.ticket_booker() # Object of ticket_booker class
    bk=backend.backend()
    loop=True
    while loop:
        print("Press the key")
        n=int(input("1. Book Ticket \n2. Cancel Ticket \n3. Display Booked Tickets \n4. Display Available Tickets \n5. Exit \n->"))

        if n == 1:
            if bk.Available_Tickets<=0:
                print("Tickets are sold out!")
            else:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                berth_preference = input("Enter Berth Preference (Lower/Middle/Upper):")
                tb.Book_Ticket(name, age, berth_preference)
        elif n == 2:
            id=int(input("Enter the ID:"))
            tb.Cancel_Ticket(id)
        elif n == 3:
            tb.Display_Booked_Tickets()
        elif n == 4:
            tb.Display_Available_Tickets()
        elif n == 5:
            loop = False
            exit()






