N=int(input())
nothing=1

for i in range(1,N+1):
    if i==1:
        print(' '*(N-i)+'*')
        
    elif i==N:
        print('*'+nothing*'*' +'*')
    else:
        print(' '*(N-i)+'*'+nothing*' ' +'*')
        nothing +=2

