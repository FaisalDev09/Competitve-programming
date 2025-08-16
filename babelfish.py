# Empty dict to store translations
mydict = {}

# Read the dictionary input until an empty line
while True:
    line = input()
    if line.strip() == "":
        break
    
    english,foreign = line.split()
    mydict[foreign] = english

# Read the words to translate until the end of input (EOF)
while True:
    try:
        word = input()
    except EOFError:
        break
    
    # Print the English translation if it exists, otherwise prin "eh"
    print(mydict.get(word,"eh"))




    
