A,B=map(int, input().split())

print(A,B,end=" ")
for i in range(8):
    C=(A+B)%10
    print(C,end=" ")
    A,B = B,C