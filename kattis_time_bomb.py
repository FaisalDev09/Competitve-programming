# Mapping of each digit's ASCII 3x5 pattern to the actual digit
digits = {
    ("***",
     "* *",
     "* *",
     "* *",
     "***"): "0",
    ("  *",
     "  *",
     "  *",
     "  *",
     "  *"): "1",
    ("***",
     "  *",
     "***",
     "*  ",
     "***"): "2",
    ("***",
     "  *",
     "***",
     "  *",
     "***"): "3",
    ("* *",
     "* *",
     "***",
     "  *",
     "  *"): "4",
    ("***",
     "*  ",
     "***",
     "  *",
     "***"): "5",
    ("***",
     "*  ",
     "***",
     "* *",
     "***"): "6",
    ("***",
     "  *",
     "  *",
     "  *",
     "  *"): "7",
    ("***",
     "* *",
     "***",
     "* *",
     "***"): "8",
    ("***",
     "* *",
     "***",
     "  *",
     "***"): "9",
}

# Read 5 rows of ASCII input
rows = [input() for _ in range(5)]

# Each digit is 3 column wide + 1 space = 4 char
n_digits = (len(rows[0]) + 1) // 4

# Build the number as a string
number = ""  

for d in range(n_digits):
    digit_block = []
    for r in range(5):
        digit_block.append(rows[r][d*4 : d*4+3])
    pattern = tuple(digit_block)
    
    # If the block does not match any digit, fail immediately
    if pattern not in digits:
        print("BOOM!!")
        exit()
    
    # Otherwise, append the recognized digit
    number += digits[pattern]

# After building the whole number, check divisibility by 6
if int(number) % 6 == 0:
        print("BEER!!")
else:
    print("BOOM!!")

