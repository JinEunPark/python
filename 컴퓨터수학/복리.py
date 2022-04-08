sum = 0
a1 = 10000
for i in range(20):
    sum = 1.03*(sum+10000)
    print(sum)

sum2 = 0
for i in range(1,20):
    sum2 += i*(i+1)
print(sum2)
sum3 = 0
for i in range(1,11):
    sum3+= i**3 - i
print(sum3)

# a1 = 1
# an = a1
#
# for i in range(1,101):
#     anp1 = an / (2 * an + 1)
#     an = anp1
# print(an)

a1 = 1
a2 = 4
an = a1
anp1 = a2
for i in range(1,100):
    anp2 = 3*anp1-2*an
    an = anp1
    anp1 = anp2

    print(an)
print(an)