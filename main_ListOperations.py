import module_ListFunction as lf

size=int(input("Please enter the number of elements required in the list: "))
if size<0:
    print("Invalid number of elements!")
    exit()
elif size==0:
    print("Empty List!")
    exit()
else:
    L=[]
    for i in range(size):
        temp=int(input("Enter the element: "))
        L.append(temp)
print("The list: ",L)
print("The maximum value in the list: ",lf.maxL(L))
print("The minimum value in the list: ",lf.minL(L))
print("The sum of the elements in the list: ",lf.sumL(L))
print("The average of the elements: ",lf.avgL(L))
print("The median of the list: ",lf.medianL(L))


