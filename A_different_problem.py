while True:
    try:
      num_1, num_2 = map(int,input().split()) 
      ans = abs((num_1) - (num_2)) # absolute value of the answer to get a posstive number
    except EOFError: 
        break
    except ValueError:
        break
    print(ans)



    
