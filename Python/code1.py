print("Enter your string: ")
usrInput = input()
vowels = 0
consonant = 0

# Using for loop to loop in Vowels.
for i in usrInput:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels+1
    else:
        consonant = consonant+1

length = len(usrInput)  # Used len command to find out the length of a string.
print("Length is %s" % length)
print("Number of vowels are: %s " % vowels)
# Got a type error for consonant TypeError: can only concatenate str (not "int") to str.
print("Number of consonants are: " + str(consonant))
# So did a google search and found out what it meant and how to fix it!
