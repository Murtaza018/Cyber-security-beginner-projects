from nltk.corpus import words
import math

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
def get_position(char, keyboard_rows):
    for row_index, row in enumerate(keyboard_rows):
        if char in row:
            col_index = row.index(char)
            return (row_index, col_index)
    return None  

def is_adjacent(pos1, pos2):
    if not pos1 or not pos2:
        return False
    row_diff = abs(pos1[0] - pos2[0])
    col_diff = abs(pos1[1] - pos2[1])
    return row_diff <= 1 and col_diff <= 1
def has_keyboard_pattern(password, keyboard_rows):
    password = password.lower()
    positions = [get_position(c, keyboard_rows) for c in password]

    count = 1
    for i in range(1, len(positions)):
        if is_adjacent(positions[i-1], positions[i]):
            count += 1
            if count >= 3:
                return True  
        else:
            count = 1 
    return False

keyboard_rows = [
    "1234567890",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]

if has_keyboard_pattern(password, keyboard_rows):
    print("Password contains a keyboard pattern (like 'qwe')")
else:
    print("No keyboard pattern detected")

#implement check for repeated patterns like aaa bbb abcabc

def has_repeated_characters(password, threshold=3):
    count = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            count += 1
            if count >= threshold:
                return True
        else:
            count = 1
    return False

def has_repeated_pattern(password):
    length = len(password)
    for size in range(1, length // 2 + 1):
        if length % size == 0:
            substring = password[:size]
            if substring * (length // size) == password:
                return True
    return False

if has_repeated_characters(password):
    print("Password contains repeated characters (e.g., 'aaaa')")

if has_repeated_pattern(password):
    print("Password contains repeated pattern (e.g., 'abcabcabc')")


charset=(uppercase*26) + (lowercase*26) +(digit*10) +(special*32)
entropy=length* math.log2(charset)
if entropy <40:
    print("Password Entropy Value is weak")
elif entropy <60:
    print("Password Entropy Value is moderate")
else:
    print("Password Entropy Value is high")