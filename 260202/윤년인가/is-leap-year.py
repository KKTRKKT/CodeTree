Y = int(input())

print("true" if Y % 4 == 0 and not (Y % 100 == 0 and Y % 400 != 0) else "false")