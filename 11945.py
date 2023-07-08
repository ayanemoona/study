N,M=map(int,input().split())
A=[]
for _ in range(N):
    b=list(input())
    b.reverse()
    if len(b)==M:
        A.append(b)
for i in range(N):

    print(''.join(A[i]))