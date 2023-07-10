S,K,H=map(int,input().split())
if S+K+H >= 100:
    print("OK")
elif S+K+H<100:
    A=[S,K,H]
    A.sort()
    if A[0]==S:
        print("Soongsil")
    elif A[0]==K:
        print("Korea")
    elif A[0]==H:
        print("Hanyang")