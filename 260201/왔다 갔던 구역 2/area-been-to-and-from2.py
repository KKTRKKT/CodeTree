"""
N번의 명령이 주어짐,
x R과 x L,
2번 이상 지나간 크기,

list 2000
"""
from pkgutil import resolve_name

N = int(input())
commands = [list(input().split()) for _ in range(N)]

arr = [0] * 2001

start = 1001
current = 0

for command in commands:
    arr[start+current] += 1
    x = int(command[0])
    dir = command[1]
    for i in range(x):
        if command[1] == "R":
            current += 1
        else:
            current -= 1
        arr[start+current] += 1

result = 0
num = 0
for v in arr:
    if(v > 1):
        num += 1
    else:
        if num > 1:
            result += num-1
            num = 0
print(result)
