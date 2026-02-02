N = input()
arr = list(map(int, input().split()))
print(*[e**2 for e in arr])