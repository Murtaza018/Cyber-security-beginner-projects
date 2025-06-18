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
print("Select Algorithm")
print("0-Use All Algorithms")    
print("1-Caeser Cipher")    
print("2-Vigenere Cipher")    
print("3-XOR")    
if opt==1:
    print("Encryption!")    
if opt==2:
    print("Decryption!")    