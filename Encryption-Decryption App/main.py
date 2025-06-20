def selectType():
    opt=int(input("Enter Type:Encryption(1)/Decryption(2):"))
    if(opt==1 or opt==2):
        return opt
    else:
        print("Invalid Option!")    
    return -1

def selectAlgorithm():
    print("Select Algorithm")
    print("0-Use All Algorithms")    
    print("1-Caeser Cipher")    
    print("2-Vigenere Cipher")    
    print("3-Atbash Cipher")    
    print("4-XOR")    
    print("5-ROT13")
    opt=int(input("Enter option:")) 
    return opt

msg=input("Enter message:")
opt=0
while opt!=1 or opt!=2:
    opt=selectType()
opt2=-1
while opt2<0 or opt2>5:
    opt2=selectAlgorithm()

if opt2==0:
    print("All algorithms")
elif opt2==1:
    print("Caeser Cipher")
elif opt2==2:
    print("Vigenere Cipher")
elif opt2==3:
    print("Atbash Cipher")
elif opt2==4:
    print("XOR")
elif opt2==5:
    print("ROT13")
        