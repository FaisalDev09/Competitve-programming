name = input("")

res = []
last = ""
for char in name:
    if char != last:
        res.append(char)   
        last = char
print(*res,sep="")
   

        
