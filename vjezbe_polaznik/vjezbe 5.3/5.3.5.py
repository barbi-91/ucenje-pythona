dan= int(input("Dan:"))
mjesec=int(input("Mjesec"))
godina=int(input("Godina"))

if dan> 0 and dan <31 and mjesec >0 and mjesec <12 and godina>0 and godina <2020:
    if mjesec==1:
       mj="sijecanj"
    elif mjesec==2:
        mj="veljca"
    elif mjesec==3:
       mj="ozujak"
    elif mjesec==4:
        mj="travanj"
    elif mjesec==5:
        mj="svibanj"
    elif mjesec==6:
       mj="lipanj"
    elif mjesec==7:
        mj="srpanj"
    elif mjesec==8:
        mj="kolovoz"
    elif mjesec==9:
        mj="rujan"
    elif mjesec==10:
       mj="listopad"
    elif mjesec==11:
        mj="studeni"
    elif mjesec==12:
        mj="prosinac"
    print(dan,".", mj,"," ,godina,".", sep="")


else:
    print("pogreska unosa")
