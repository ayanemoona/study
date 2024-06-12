N=int(input())
result=[]
for i in range(N):
    A=input()
    B=str(i+1)+". "+A
    result.append(B)
for i in result:
    print(i)