def sollution(n):
    l=[]
    result=0
    for i in range(len(n)):
        tmp_l=[]
        try:
            for j in range(i,i+3):
                tmp_l.append(n[j])
        except:
            break

        l.append(max(tmp_l))
    
    return l
    




n=list(map(int,input().split(" ")))
print(* sollution(n))
# print(n)