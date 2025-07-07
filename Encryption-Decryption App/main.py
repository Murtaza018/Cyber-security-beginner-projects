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
def CaeserEncryptNum(msg,shift):
    encrypted = ""
    for char in msg:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted
  

def CaeserEncryptRange(msg,shift_lower,shift_upper):
    encrypted_range=[]
    for j in range(shift_lower,shift_upper):
        encrypted_range.append(CaeserEncryptNum(msg,j))
    return encrypted_range    

def CaeserDecryptNum(msg,shift):
    return CaeserEncryptNum(msg,-shift)

def CaeserDecryptRange(msg,shift_lower,shift_upper):
    decrypted_range=[]
    for j in range(shift_lower,shift_upper):
        decrypted_range.append(CaeserEncryptNum(msg,-j))
    return decrypted_range

def CaeserCipher(msg,opt):
    opt2=-1
    while opt2!=0 and opt2!=1:
        opt2=int(input("Enter shift number(0) or shift range(1):"))
    if(opt2==0):
        shift=int(input("Enter shift number:"))
        if opt==1:
            encrypted_num=CaeserEncryptNum(msg,shift)  
            print(f"Encryption with Caesar Cipher using shift={shift}: {encrypted_num}")  
        elif opt==2:
            decrypted_num=CaeserDecryptNum(msg,shift)   
            print(f"Decryption with Caesar Cipher using shift={shift}: {decrypted_num}")      

    else:
        shift_lower=int(input("Enter lower shift number:"))    
        shift_upper=int(input("Enter upper shift number:"))  
        if opt==1: 
            encrypted_range=CaeserEncryptRange(msg,shift_lower,shift_upper)  
            print(f"Encryption with Caesar Cipher using shift range={shift_lower}-{shift_upper}: {encrypted_range}") 
        elif opt==2:
            decrypted_range=CaeserDecryptRange(msg,shift_lower,shift_upper)  
            print(f"Decryption with Caesar Cipher using shift range={shift_lower}-{shift_upper}: {decrypted_range}")  
def VigenereCipherEncrypt(msg, key):
    encrypted = ""
    key_index = 0
    key = key.lower() 

    for char in msg:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            encrypted += char

    return encrypted

def VigenereCipherDecrypt(msg,key):
    print("Vigenere Decrypt")    
def VigenereCipher(msg,opt):
    opt2=-1
    while opt2!=0 and opt2!=1:
        opt2=int(input("Use Default Key(0) or Customized Key(1):"))
    if opt2==0:
        key="KEY"
    else:
        key=str(input("Enter Key:"))    
    if opt==1:
        encrypted_default_msg=VigenereCipherEncrypt(msg,key)
        print(f"Encryption with Vigenere Cipher using Default Key: {encrypted_default_msg}") 
    elif opt==2:
        decrypted_default_msg=VigenereCipherDecrypt(msg,key)
        print(f"Decryption with Vigenere Cipher using Default Key: {decrypted_default_msg}") 



msg=input("Enter message:")
opt=0
while opt!=1 and opt!=2:
    opt=selectType()
opt2=-1
while opt2<0 or opt2>5:
    opt2=selectAlgorithm()

if opt2==0:
    print("All algorithms")
elif opt2==1:
    CaeserCipher(msg,opt)
elif opt2==2:
    VigenereCipher(msg,opt)
elif opt2==3:
    print("Atbash Cipher")
elif opt2==4:
    print("XOR")
elif opt2==5:
    print("ROT13")
        