import taxi_booker

if __name__=="__main__":
    loop = True
    tb = taxi_booker.taxi_booker()

    while loop:
        print("Press the Key")
        n = int(input("1. Book Taxi \n2. Display Taxi Details \n3. Exit \n--> "))
        if n == 1:
            pickup=input("Enter the Pickup point: ")
            drop=input("Enter the Drop point: ")
            time=int(input("Enter the Pickup time: "))
            tb.Book_Taxi(pickup,drop,time)

        elif n == 2:
            tb.Display_Taxi_Details()
        elif n == 3:
            loop = False
            print("Have a nice day:)")
            exit()
        else:
            print("Invalid Input!")


