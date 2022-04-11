import matplotlib.pyplot as plt

def cola(an):
    if an % 2 == 0:
        anp1 = an / 2
        return anp1
    elif an % 2 == 1:
        anp1 = 3 * an + 1
        return anp1


an = 109
anlist = []
nlist = []
anlist.append(an)
nlist.append(1)


for i in range(1, 100001):
    anp1 = cola(an)
    an = anp1
    if an == 1:
        print("an = 1 , n = ", i)
        break
    anlist.append(anp1)
    nlist.append(i+1)
plt.plot(nlist, anlist,'-o')
plt.show()
