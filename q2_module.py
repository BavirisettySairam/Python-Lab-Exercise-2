def add(S,ele):
    if ele not in S:
        S.add(ele)
        return S
    else:
        print("Element already part of set.")
        return S

def rem(S,ele):
    if ele in S:
        S.remove(ele)
        return S
    else:
        print("Element isn't part of set.")
        return S

def union(S,T):
    if len(S)==0:
        return T
    elif len(T)==0:
        return S
    for i in T:
        if i not in S:
            S=add(S,i)
    return S

def inter(S,T):
    if len(S)==0:
        return S
    elif len(T)==0:
        return T
    for i in S:
        if i not in T:
            S=rem(S,i)
    return S

def S1diffS2(S1,S2):
    if len(S1)==0:
        return S1
    elif len(S2)==0:
        return S2
    for i in S1:
        if i in S2:
            S1.remove(i)
    return S1    

def S1subS2(S1,S2):
    if (len(S1)==0):
        return 1
    elif (len(S2)==0):
        if (len(S1)==0):
            return 1
        else:
            return 0
    for i in S1:
        if i not in S2:
            return 0
    return 1    

def leng(S):
    s=0
    for i in S:
        s=s+1
    return s

def symdiff(S1,S2):
    return (union(S1,S2)-inter(S1,S2))

def pow(S):
    return (2**leng(S))

