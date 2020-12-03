km = int(input())
rs = 0
if(km>75):
    rs = km *8
    print("mini",rs)
elif(km<=3):
    print("mini",50)
else:
    dup = km-18
    if(dup>0):
        rs = 200+(km-18)*8
    else:
        rs = 50 + (km-3)*10
    print("mini",rs)
rs=0
if(km>100):
    rs = km*10
    print("sedan",rs)
elif(km<=5):
    print("sedan",80)
else:
    du = km - 20
    if(du>0):
        rs = 260 + (km-20)*10
    else:
        rs = 80 +(km-5)*12
    print("sedan",rs)
rs =0
if(km<=5):
    print("suv",100)
else:
    du = km-20
    if(du>0):
        rs = 325 + (km-20)*12
    else:
        rs = 100 + (km-5)*15
    print("suv",rs)
