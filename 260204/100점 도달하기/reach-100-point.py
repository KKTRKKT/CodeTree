score = int(input())
for i in range(score, 101):
    print('A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F', end=" ")
    score += 1