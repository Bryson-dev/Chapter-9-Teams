import string
def main():
    #main calls all other functions to build the entire program
   
   
    shift = get_shift()
    message = get_message()
    key = create_key(shift)
   
    choice = choose_option()
   
    if choice == True:
        print('\nNOW RUNNING ENCODE\n')
        encode(message, key)
    else:
        print('\nNOW RUNNING DECODE\n')
        decode(message, key)
   
   
def get_shift():
    #get_shift will prompt the user for the shift value and return the value as a string
    inpv = True
    while inpv == True:
       
        shift = input('Please enter a number from 1 - 25 for the encoding number: ')
        if shift.isdigit() == True:
            shift = int(shift)
            if shift in range(1,26):
                return shift
           
            else:
                print()
                print('ERROR!')
                print('Only numbers between 1-25\n')
                shift = 0
                inpv = True
                

   

def choose_option():
    #It will return True if the user chooses encode and False if the user chooses decode.
    choice = input('Would you like to encode or decode: ')
    if choice == 'encode':
        try:
            return True
        except ValueError:
            print('Invalid input choose a valid option')
           
    if choice == 'decode':
        try:
            return False
        except ValueError:
            print('Invalid input choose a vlid option')
   
    pass

def get_message():
    #get_message will prompt the user to enter a message to encode or decode
    
    naughty = 0
    
    message = input('Enter a message: ')
    for letter in message:
        if letter in string.ascii_lowercase and string.ascii_uppercase:
            naughty = 0
        else:
            naughty += 1
    if naughty == 0:
        return message
    else:
        print('please enter a valid message twin')

def create_key(shift):
    #It should create the caesar cipher according to the shift value and store the key in a dictionary and return the dictionary as the key
   
    key = {}
    count = 1
    uppercase = {}
    lowercase = {}
   
    for letter in string.ascii_uppercase:
        uppercase[letter] = count
        count += 1
       
       

    count = 1
    for letter in string.ascii_lowercase:
        lowercase[letter] = count
        count += 1
       
    count = 1
    for letter in uppercase:
        value = uppercase[letter]
        value = value + shift
        if value > 26:
            value = value % shift
       
        key[letter] = value
    for letter in lowercase:
        value = lowercase[letter]
        value = value + shift
        if value > 26:
            value = value % shift
       
        key[letter] = value
   
    return key
   
   
   
   

def encode(message, key):
    #encode accepts message as a string and key as a dictionary
    
    coded = ""

    for cha in message:
        if cha in key:
            num = key[cha]  
           
            
            if cha.isupper():
                letter = string.ascii_uppercase[num - 1]
            else:
                letter = string.ascii_lowercase[num - 1]
           
            coded += letter
        else:
            
            coded += cha

    print(coded)
    return coded
   
           
           

def decode(message, key):
    #decode accepts message as a string and key as a dictionary
    #It should decode the message using the key and return the decoded message as a string
    decoded = ""


    rev_up = {}
    rev_low = {}

    for letter in string.ascii_uppercase:
        rev_up[key[letter]] = letter

    for letter in string.ascii_lowercase:
        rev_low[key[letter]] = letter

    for cha in message:
        if cha.isupper() and cha in string.ascii_uppercase:
            num = string.ascii_uppercase.index(cha) + 1
            decoded += rev_up[num]
        elif cha.islower() and cha in string.ascii_lowercase:
            num = string.ascii_lowercase.index(cha) + 1
            decoded += rev_low[num]
        else:
            decoded += cha

    print(decoded)
    return decoded

main()

