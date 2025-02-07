def currencyCounter(amount):
    notes=[2000,500,200,100,50,20,10,5,1]
    noteCounter=[0]*len(notes)

    for i in range(len(notes)):
        if(amount>=notes[i]):
            noteCounter[i]=amount//notes[i]
            amount=amount%notes[i]

    #print
    print("Currency Counter")
    for i in range(len(notes)):
        if(noteCounter[i]!=0):
            print(notes[i]," : ",noteCounter[i])


currencyCounter(255)
