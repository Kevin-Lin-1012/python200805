names=[]
scores=[]
total=0
C=int(input('輸入人數'))
for a in range(C):
    A=input('輸入名字')
    B=int(input('輸入分數'))
    names.append(A)
    scores.append(B)
    print()
def tot(C,total):
    for b in range(C):
        total=total+scores[b]
    return total
print('總分是',tot(C,total))
def avg(tot,C):
    return tot/C
print('平均是',avg(tot(C,total),C))
def highest(C,scores,names):
    highest=0
    highest_name=''
    for c in range(C):
         if scores[c]>highest:
             highest=scores[c]
             highest_name=names[c]
    print('最高分',highest,'是',highest_name,'的')
    return
highest(C,scores,names)                   
def lowest(C,scores,names):
    lowest=100
    lowest_name=''
    for c in range(C):
         if scores[c]<lowest:
             lowest=scores[c]
             lowest_name=names[c]
    print('最低分',lowest,'是',lowest_name,'的')
    return
lowest(C,scores,names)                   

        

    






