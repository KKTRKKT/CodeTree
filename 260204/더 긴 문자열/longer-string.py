str1, str2 = input().split()
long_str = str1 if len(str1) > len(str2) else str2
print(long_str, len(long_str))