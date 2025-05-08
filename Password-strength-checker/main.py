password=input("Enter password:")
print("password:",password)
length=len(password)
print("length:",length)
if length < 8:
    print("Password is too short")
if length> 25:
    print("Password is too long")  
char_list=[]    
for char in password:
    if char not in char_list:
        char_list.append(char)
char_list_length=len(char_list)        
print("char_list length:",char_list_length)
if char_list_length < length/2:
    print("Character Variety is Low")        
if char_list_length >= length/2 and char_list_length<3*length/4:
    print("Character Variety is Medium")        
if char_list_length >= 3*length/4:
    print("Character Variety is High")        