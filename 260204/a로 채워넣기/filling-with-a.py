str1 = input()

lst = list(str1)
lst[1] = 'a'
lst[-2] = 'a'

print("".join(lst))