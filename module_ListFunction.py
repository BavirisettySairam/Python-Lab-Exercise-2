def maxL(L):
    if (len(L)==0):
        return None
    max=L[0]
    for i in L:
        if i>max:
            max=i
    return max

def minL(L):
    if (len(L)==0):
        return None
    min=L[0]
    for i in L:
        if i<min:
            min=i
    return min

def sumL(L):
    sum=0
    for i in L:
        sum=sum+i
    return sum

def avgL(L):
    suml=sumL(L)
    avg=suml/(len(L))
    return (avg)

def medianL(L):
    L.sort()
    if ((len(L)%2)==0):
        med=((L[int(len(L)/2)-1]+L[int(len(L)/2)])/2)
        return med
    else:
        return L[int(len(L)/2)+1]