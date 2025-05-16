from nltk.corpus import words

print("Initializing System")
english_words = set(words.words())

common_passwords = set()
with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        common_passwords.add(line.strip())

print("System Initialized")
password=input("Enter password:")
print("password:",password)
length=len(password)
print("length:",length)
if length < 10:
    print("Password length is too short(must be longer)")
elif length> 25:
    print("Password length is long(Good)")  
else:    
    print("Password length is moderate(can be longer)")  

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
    print("Character Variety is Low,(must be higher)")        
if char_list_length >= length/2 and char_list_length<3*length/4:
    print("Character Variety is Moderate(can be higher)")        
if char_list_length >= 3*length/4:
    print("Character Variety is High(Good)")   


if uppercase/length>=0.2:
    print("Uppercase quantity is High(Good)")
elif uppercase/length<0.2 and uppercase/length>0.1:
    print("Uppercase quantity is Moderate(can be higher)")
else:
    print("Uppercase quantity is Low(must be higher)")


if lowercase/length>=0.2:
    print("Lowercase quantity is High(Good)")
elif lowercase/length<0.2 and lowercase/length>0.1:
    print("Lowercase quantity is Moderate(can be higher)")
else:
    print("Lowercase quantity is Low(must be higher)")


if digit/length>=0.2:
    print("Digit quantity is High(Good)")
elif digit/length<0.2 and digit/length>0.1:
    print("Digit quantity is Moderate(can be higher)")
else:
    print("Digit quantity is Low(must be higher)")


if special/length>=0.2:
    print("Special Characters quantity is High(Good)")
elif special/length<0.2 and special/length>0.1:
    print("Special Characters quantity is Moderate(can be higher)")
else:
    print("Special Characters is Low(must be higher)")


common_passwords = set()
with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        common_passwords.add(line.strip())

if password in common_passwords:
    print("Password is a commonly used password.")

count=0
for common_password in common_passwords:
    if common_password in password:
        count+=1
print(f"This password contains {count} commonly used password(s)")


for i in range(len(password)):
    for j in range(i + 4, len(password) + 1):
        if password[i:j].lower() in english_words:
            print(f"Contains dictionary word: {password[i:j]}")
            break
