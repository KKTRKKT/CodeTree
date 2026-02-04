str1, str2 = input().split()
long_str = str1 if len(str1) > len(str2) else str2 if len(str2) > len(str1) else 'same'
print(*[long_str, len(long_str)] if long_str != 'same' else [long_str])