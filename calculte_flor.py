def calcualteFloor(move:str)->int:
    """count what felor go"""
    move=list(move)
    print(move)

    if len(move)!=4:
        raise Exception
    
    a=0
    for i in move:
        i=i.capitalize()
        print(i)
        if i=="U":
            a+=1
        if i=="D":
            a-=1
    print ("floor :",a)

calcualteFloor("dddu")