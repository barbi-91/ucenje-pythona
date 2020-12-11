HrvEngrijecnik= {}
HrvEngrijecnik= {
    "macka":"cat",
    "pas":"dog",
    "cvijet":"flower",
    "kosa":"hair",
    "djevojka":"girl",
    "cesta":"road"
}
while 1==1: #while true
    rijec=input("unesi rijec na hrvatskom:")
    rijec= rijec.lower()

    if rijec =="x":
        break
    if rijec in HrvEngrijecnik:
        print(HrvEngrijecnik[rijec])
    else:
        print("rijec se ne nalazi u rijecniku")