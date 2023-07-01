# 백준 15727
L=int(input())
t=0
t+=L//5
if L%5!=0:
    t+=1
print(t)