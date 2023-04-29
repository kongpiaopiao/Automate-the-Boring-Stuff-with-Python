import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    lis=[]
    for i in range(100):
        x=random.randint(0, 1)
        lis.append(x)
        #print(lis)

    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(95):
        x1 = (i + 1)
        x2 = (i + 2)
        x3 = (i + 3)
        x4 = (i + 4)
        x5 = (i + 5)
        if lis[i]==lis[x1] and lis[i]==lis[x2] and lis[i]==lis[x3] and lis[i]==lis[x4] and lis[i]==lis[x5]:
            numberOfStreaks = numberOfStreaks+1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
