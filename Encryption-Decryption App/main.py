def selectType():
    opt=input("Enter Type:Encryption(1)/Decryption(2):")
    if(opt==1 or opt==2):
        return opt
    else:
        print("Invalid Option!")    
    return -1


msg=input("Enter message:")
opt=0
while opt!=1 or opt!=2:
    opt=selectType()
if opt==1:
    print("Encryption!")    
if opt==2:
    print("Decryption!")    