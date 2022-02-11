n1 = 1
n2 = 1
n3 = 1

for i in range(1, 21):
    if i < 3:
        n3 = 1
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    if n3 < 20:
        print(n3)