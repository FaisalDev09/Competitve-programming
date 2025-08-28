while True:
    n = int(input()) 
    if n == 0:
        break

    students = [] 

    for i in range(n):
        name = input()
        students.append(name)
    
    # Sort by the first two letters - with lambda function
    sorted_students =  sorted(students, key=lambda w:w[:2]) 
    for j in sorted_students:
        print(j)





