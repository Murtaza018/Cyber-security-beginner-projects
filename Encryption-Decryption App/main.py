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

def VigenereCipherDecrypt(msg, key):
    decrypted = ""
    key = key.lower()
    key_index = 0

    for char in msg:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted += decrypted_char
            key_index += 1
        else:
            decrypted += char 

    return decrypted
  
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

def AtbashCipherFunction(msg):
    result = ""
    for char in msg:
        if char.isupper():
            result += chr(ord('Z') - (ord(char) - ord('A')))
        elif char.islower():
            result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char  # Keep spaces, punctuation unchanged
    return result

def AtbashCipher(msg,opt):
    Cipher_msg=AtbashCipherFunction(msg)
    if opt==1:
        print(f"Encryption with Atbash Cipher: {Cipher_msg}") 
    elif opt==2:
        print(f"Decryption with Atbash Cipher: {Cipher_msg}") 

def XORCipher(msg, mode):
  
    opt2 = -1
    while opt2 != 0 and opt2 != 1:
        opt2 = int(input("Use Default Key(0) or Customized Key(1): "))

    key = "KEY" if opt2 == 0 else input("Enter Key: ")

    result = ""
    for i in range(len(msg)):
        result += chr(ord(msg[i]) ^ ord(key[i % len(key)]))

    if mode == 1:
        print(f"\nEncryption with XOR Cipher using {'Default' if opt2 == 0 else 'Customized'} Key: {result}")
    elif mode == 2:
        print(f"\nDecryption with XOR Cipher using {'Default' if opt2 == 0 else 'Customized'} Key: {result}")

def ROT13Cipher(msg,opt):
    if opt==1:
        encrypted=CaeserEncryptNum(msg,13)
        print(f"Encryption with ROT13 Cipher: {encrypted}") 
    if opt==2:
        decrypted=CaeserEncryptNum(msg,-13)
        print(f"Decryption with ROT13 Cipher: {decrypted}")

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
    AtbashCipher(msg,opt)
elif opt2==4:
    XORCipher(msg,opt)
elif opt2==5:
    print("ROT13")
        