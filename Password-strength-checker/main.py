password=input("Enter password:")
print("password:",password)
length=len(password)
print("length:",length)
if length < 10:
    print("Password is too short")
if length> 25:
    print("Password is too long")  
char_list=[]
uppercase=0    
lowercase=0    
digit=0
special=0    
for char in password:
    if char not in char_list:
        char_list.append(char)
    if char.isupper():
        uppercase+=1    
    elif char.islower():
        lowercase+=1    
    elif char.isdigit():
        digit+=1   
    else:
        special+=1
             
char_list_length=len(char_list)        
print("char_list length:",char_list_length)
if char_list_length < length/2:
    print("Character Variety is Low")        
if char_list_length >= length/2 and char_list_length<3*length/4:
    print("Character Variety is Medium")        
if char_list_length >= 3*length/4:
    print("Character Variety is High")          