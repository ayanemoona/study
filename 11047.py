N,K=map(int,input().split())
coin=[]
result=0
for i in range(N):
    A=int(input())
    coin.append(A)


for i in range(N-1,-1,-1):
    result+=K//coin[i]
    K=K%coin[i]
print(result)    