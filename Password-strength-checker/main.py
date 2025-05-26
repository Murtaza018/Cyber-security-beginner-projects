from nltk.corpus import words
import math

def initializeSystem():
    print("Initializing System")
    english_words = set(words.words())

    common_passwords = set()
    with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            common_passwords.add(line.strip())

    print("System Initialized")
    return common_passwords,english_words

def password_input():
    password=input("Enter password:")
    return password
def passwordVarietyValue(password):
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
    return char_list,uppercase,lowercase,digit,special
        
def length_checker(length):
    if length < 8:
        print("Password length is too short(must be longer)")
        return 5
    elif length> 20:
        print("Password length is long(Good)")  
        return 20
    else:    
        print("Password length is moderate(can be longer)")  
        return 12.5

def characterVarietyCheck(length,uppercase,lowercase,digit,special,char_list): 
    score=0
    char_list_length=len(char_list)        
    print("char_list length:",char_list_length)
    if char_list_length < length/2:
        print("Character Variety is Low,(must be higher)")   
        score+=1     
    if char_list_length >= length/2 and char_list_length<3*length/4:
        print("Character Variety is Moderate(can be higher)")    
        score+=3    
    if char_list_length >= 3*length/4:
        print("Character Variety is High(Good)") 
        score+=5  


    if uppercase/length>=0.2:
        print("Uppercase quantity is High(Good)")
        score+=5
    elif uppercase/length<0.2 and uppercase/length>0.1:
        print("Uppercase quantity is Moderate(can be higher)")
        score+=3
    else:
        print("Uppercase quantity is Low(must be higher)")
        score+=1


    if lowercase/length>=0.2:
        print("Lowercase quantity is High(Good)")
        score+=5
    elif lowercase/length<0.2 and lowercase/length>0.1:
        print("Lowercase quantity is Moderate(can be higher)")
        score+=3
    else:
        print("Lowercase quantity is Low(must be higher)")
        score+=1


    if digit/length>=0.2:
        print("Digit quantity is High(Good)")
        score+=5
    elif digit/length<0.2 and digit/length>0.1:
        print("Digit quantity is Moderate(can be higher)")
        score+=3
    else:
        print("Digit quantity is Low(must be higher)")
        score+=1


    if special/length>=0.2:
        print("Special Characters quantity is High(Good)")
        score+=5
    elif special/length<0.2 and special/length>0.1:
        print("Special Characters quantity is Moderate(can be higher)")
        score+=3
    else:
        print("Special Characters is Low(must be higher)")
        score+=1
    return score

def commonPasswordCheck(password,common_passwords):
    score=0
    if password in common_passwords:
        print("Password is a commonly used password.")
        score+=1
    else:
        score+=3    

    count=0
    for common_password in common_passwords:
        if common_password in password:
            count+=1
    print(f"This password contains {count} commonly used password(s)")
    if count <=12:
        score+=12-count
    return score    

def dictionaryWordCheck(password,english_words):
    score=10
    for i in range(len(password)):
        for j in range(i + 4, len(password) + 1):
            if password[i:j].lower() in english_words:
                print(f"Contains dictionary word: {password[i:j]}")
                score=2.5
                break
    return score     
   
def keyboardPattern(password):
    def get_position(char, keyboard_rows):
        for row_index, row in enumerate(keyboard_rows):
            if char in row:
                return (row_index, row.index(char))
        return None  

    def is_adjacent(pos1, pos2):
        if not pos1 or not pos2:
            return False
        row_diff = abs(pos1[0] - pos2[0])
        col_diff = abs(pos1[1] - pos2[1])
        return row_diff <= 1 and col_diff <= 1
    
    keyboard_rows = [
        "1234567890",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]
    score=10
    password = password.lower()
    positions = [get_position(c, keyboard_rows) for c in password]

    count = 1
    in_pattern = False

    for i in range(1, len(positions)):
        if is_adjacent(positions[i - 1], positions[i]):
            count += 1
            if count >= 3 and not in_pattern:
                in_pattern = True  # avoid counting overlapping
                score-=2
        else:
            count = 1
            in_pattern = False  # reset flag for a new pattern
    return score

def has_repeated_characters(password, threshold=3):
    count = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            count += 1
            if count >= threshold:
                print("Password contains repeated characters (e.g., 'aaaa')")
                return 2
        else:
            count = 1
    print("Password does not contain repeated characters (e.g., 'aaaa')")
    return 5

def has_repeated_pattern(password):
    score=5
    length = len(password)
    for size in range(1, length // 2 + 1):
        if length % size == 0:
            substring = password[:size]
            if substring * (length // size) == password:
                print("Password contains repeated pattern (e.g., 'abcabcabc')")
                return 2
    print("Password does not contain repeated pattern (e.g., 'abcabcabc')")
    return 5

def calculateEntropy(length,uppercase,lowercase,digit,special):
    score=0
    charset=(uppercase*26) + (lowercase*26) +(digit*10) +(special*32)
    entropy=length* math.log2(charset)
    if entropy <40:
        print("Password Entropy Value is weak")
        score=3
    elif entropy <60:
        print("Password Entropy Value is moderate")
        score=6
    else:
        print("Password Entropy Value is high")
        score=10
    return score    

def rating_evaluation(rating):
    if rating < 10:
        return "Horrible"
    if rating < 20:
        return "Extremely Weak"
    if rating < 30:
        return "Very Weak"
    if rating < 40:
        return "Weak"
    if rating < 50:
        return "Moderately Weak"
    if rating < 60:
        return "Moderate"
    if rating < 70:
        return "Moderately Strong"
    if rating < 75:
        return "Almost Strong"
    if rating < 85:
        return "Strong"
    if rating < 90:
        return "Very Strong"
    if rating < 95:
        return "Extremely Strong"
    if rating <= 100:
        return "Perfect"

common_passwords,english_words=initializeSystem()
password=password_input() 
char_list,uppercase,lowercase,digit,special=passwordVarietyValue(password)   
length=len(password)
rating=0
rating+=length_checker(length)
rating+=characterVarietyCheck(length,uppercase,lowercase,digit,special,char_list)
rating+=commonPasswordCheck(password,common_passwords)
rating+=dictionaryWordCheck(password,english_words)
rating+=keyboardPattern(password)
rating+=has_repeated_characters(password)
rating+=has_repeated_pattern(password)
rating+=calculateEntropy(length,uppercase,lowercase,digit,special)
print("Final Rating:",rating)
print("The overall password is:",rating_evaluation(rating))