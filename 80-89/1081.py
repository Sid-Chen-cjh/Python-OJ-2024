import json

n = json.loads(input())
a, b = map(int, input().split())
ans = []
for i in n:
    if a <= i["Value"] <= b:
        print(i["ID"])
