# WORKING DRAFT - permutation cipher
# it's a copy of cipher1 with some added at the bottom to focus on just letters.
# Search for 'RESTART'

# Ignore this:
def string(charlist):
    '''Turn a list of characters into a string.'''
    s = ""
    for ch in charlist:
        s = s + ch
    return s


# Step 0 (review):
# Use the shell to evaluate these expressions:
#   ord('z')
#   chr(122)
#   chr(ord('z'))
#   chr(ord('z') + 13)
# That last one isn't a regular printable character,
# so Python says the value is '\x87'.  (What's that?)
# You can confirm it doesn't print by evaluating this:
#    print('\x87')

# Suggestion: use capital letters and small values for
# keys, to avoid getting confused by unprintable characters.


# Step 1 (review):
# Have a look at this function and try it by evaluating
#   encrypt('A', 13)

def encrypt(cap, key):
    '''Encrypt a capital letter.  The key should be
       a non-negative integer.'''
    x = ord(cap) + key
    return chr(x)


# Step 2:
# Finish this function that decrypts one character.
# Reminder: it has to undo what encrypt() did.

def decrypt(char, key):
    #SOLUTION
    code = ord(char)
    return chr(code - key)

    
# Step 3:
# The following code is supposed to encrypt and decrypt
# strings, using the key 13. Try running test3() and you'll
# see it's not working.  Fix enc13() and dec13() so they work.
# Hint: First, learn how list() and string() work by evaluating
# these expressions:
#   list("howdy")
#   string(['A', 'l', 'l', ' ', 'i', 'n'])

def test():
    msg = input("Enter your secret message: ")
    print("The message is ", msg)
    secret = enc13(msg)
    print("Encrypted as ", secret)
    decipher = dec13(secret)
    print("Decrypted as ", decipher)


def enc13(msg):
    letters = list(msg) # turn string into list of chars
    key = 13
    for i in range(len(letters)):
        letters[i] = encrypt( letters[i], key )
# SOLUTION: change print to return, since this function's result
# is needed by print in test3().
    return string(letters) 


def dec13(msg):
 #   return "not the right answer"
 # SOLUTION: just like enc13() but using decrypt().
    letters = list(msg)
    key = 13
    for i in range(len(letters)):
        letters[i] = decrypt( letters[i], key )
    return string(letters)
    
# RESTART #

def letToNum(cap):
    '''Convert a capital letter (or blank) to a number in range 0 to 26.'''
    if cap == ' ':
        return 26
    else:
        return ord(cap) - ord('A')

def numToLet(num):
    '''Convert a number in range 0..26 to a letter or blank.'''
    if num == 26:
        return ' '
    else:
        return chr(num + ord('A'))

def encrypt(cap, key):
    '''Encrypt a capital letter using key (which should be in range 0..26)'''
    x = letToNum(cap) + key
    y = x % 27
    return numToLet(y)

def decrypt(cap, key):
    x = ( letToNum(cap) - key ) % 27
    return numToLet(x)

def test():
    for c in ['A', 'B', 'Z', ' ']:
        for i in [0,1,2,25,26]:
            res = decrypt(encrypt(c,i), i) 
            print(c, " enc by ", i, " works?", res==c)
            
  
    

    



    
    


    
    

    
    
