# Introduction to Caeser's cipher - part III

######################################################
# Step 1
# Run this script and figure out what it's doing.
######################################################

def string(charlist):
    '''Turn a list of characters into a string.'''
    s = ""
    for ch in charlist:  s = s + ch
    return s

print("Try the string() function::",  string(['h', 'o', 'w', 'd', 'y']) )  

print("Try the list() function::",  list("umbrella") )

print("Try them together::",  string(list("midget")) )

raise() # delete this line when you're ready to go to the next step.


######################################################
# Step 2
# Bob said to Alice:
# "Our secret is 279.  What grade did I get in math?"
# Alice sent her a message.  Bob is trying to find his
# grade.  Fix his code so it works.
######################################################

def encrypt(cap, key):
    '''Encrypt a capital letter.  The key should be
       a non-negative integer.'''
    x = ord(cap) + key
    return chr(x)

def decrypt(char, key):
    '''Decrypt a one-character message.'''
    code = ord(char)
    return chr(code - key)

secret = 279
grade = 'A'
message = encrypt(grade, secret)
print("Bob, here is your message::",  message)

print("Alice, my grade is::",  decrypt(message, 27) )  # huh? fix this!

raise()         # delete when you'ready to go on


######################################################
# Step 3:
# Alice sends Bob a long message. He's trying to
# read it but he needs you to fix his code.
######################################################

def encrypts(msg, key):
    '''Encrypt an entire string.'''
    chars = list(msg) 
    for i in range(len(chars)):
        chars[i] = encrypt( chars[i], key )
    return string(chars) 

def decrypts(msg, key):
    chars = list(msg)
    for i in range(len(chars)):
        chars[i] = decrypt( chars[i], key )
    return string(chars)

long = "Meet me at pier C"
cipher = encrypts(long, secret)
print("Hey Bob::", cipher)

print("Hi Alice, did you say::",
      decrypts("ŤżżƋķƄżķŸƋķƇ", secret)) # fix this

raise() 

######################################################
# Step 4:
# Alice sent another message, using a different key.
# Bob is trying a lot of keys.  Can you figure out
# the message she sent?
######################################################

cipher = "ª¸s¶´Ás·ÂsÇ»¼Æs¼¹sÊ¸sÊÂÅ¾sÇÂº¸Ç»¸Å"

print(decrypts(cipher, s) )

# try different keys
for k in range(0,50):
    print( decrypts(cipher, k) )
    






          



    
 


    
    


    
    

    
    
