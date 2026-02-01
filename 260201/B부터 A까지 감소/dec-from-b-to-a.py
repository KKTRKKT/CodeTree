a, b = map(int, input().split())
print(" ".join(str(i) for i in range(b, a-1, -1)))