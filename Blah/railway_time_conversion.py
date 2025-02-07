s="06:40:03AM"

hr=s[0:2]
min=s[3:5]
secs=s[6:8]
merd=s[-2:]

if(hr=='12' and merd=='AM'):
    hr='00'
    print(hr + ":" + min + ":" + secs)
elif(merd=='PM'):
    hr2 = int(hr)
    if (hr2 < 12):
        hr2 += 12
    hr3 = str(hr2)
    print(hr3 + ":" + min + ":" + secs)

else:
    print(hr + ":" + min + ":" + secs)