import json

def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(pow(x, 0.5))+1):
            if x % i == 0:
                return False
        return True

j = json.loads(input())
for i in j:
    if is_prime(i["Value"]):
        print(i["ID"])