n = int(input())
arr = list(map(int, input().split()))

print(*[arr[i] for i in range(n-1, -1, -1) if arr[i] % 2 == 0])