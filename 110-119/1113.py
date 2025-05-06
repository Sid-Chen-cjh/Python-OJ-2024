ans = input()
m = input()
score = 0
for i in range(len(ans)):
    if ans[i] == m[i]:
        score += 20
    else:
        if score >= 10:
            score -= 10
print(score)