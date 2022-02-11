hap = 0

for i in range(1, 21):
    if i % 2 == 0:
        hap += i
    else:
        continue

print("1~20까지 짝수 합:", hap)
