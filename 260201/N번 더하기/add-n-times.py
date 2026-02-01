A, N = map(int, input().split())
print("\n".join(str(A + N*i) for i in range(1, N+1)))