import matplotlib.pyplot as plt

sum = 0
for i in range(1, 11):
    sum += i ** 2 - i
print(sum)
n = 10
sum = n * (n + 1) * (2 * n + 1) / 6 - n * (n + 1) / 2
print(sum)

sum1 = 0
for i in range(1, 6):
    sum1 += i * (i ** 2 + 3)
print(sum1)

n = 5
sum1 = (n * (n + 1) / 2) ** 2 + 3 * (n * (n + 1) / 2)
print(sum1)

a1 = 109
an = a1
anp1 = an

nlist = []
nlist.append(1)
anlist = []
anlist.append(a1)

for n in range(1, 100000):
    if an % 2 == 0:
        anp1 = an / 2
    else:
        anp1 = 3 * an + 1
    nlist.append(n + 1)
    anlist.append(anp1)
    print(anp1)
    if anp1 == 1:
        print("n= ", n + 1)
        break
    an = anp1

plt.plot(nlist, anlist, '-o')
plt.show()
