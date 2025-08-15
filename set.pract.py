s = set()

#Insert elements into the set

s.add(4)
s.add(10)
s.add(7)

#Find elements "checking if an elements exists in the set"
if 4 in s:
    #To simultate C++ iterators in sorted ordet:
    sorted_list = sorted(s) # Creates a sorted list from the set
    idx = sorted_list.index(4) # find the index of 4
    if idx + 1 < len(sorted_list):#check if there is an elemnt after 4
        print(sorted_list[idx + 1]) # print the next element in sorted order

# If an element does not exist in the set
if 7 not in s:
    print('7 is not in the set')

#Remove an element
s.discard(7) # discard removes the element if it exists, does nothing otherwise

