liste1 = []
for num in range(2,100):
    for i in range(2,num):
        if (num % i) == 0:
            break
    else:
        liste1.append(num)
print(liste1)