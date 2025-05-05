class backend:
    Id=1
    Upper=1
    Lower=1
    Middle=1
    RAC=2
    Waiting_list=2
    Available_Tickets = Upper + Lower + Middle + RAC + Waiting_list

    @classmethod
    def update_available_tickets(cls):
        cls.Available_Tickets = cls.Upper + cls.Lower + cls.Middle + cls.RAC + cls.Waiting_list


