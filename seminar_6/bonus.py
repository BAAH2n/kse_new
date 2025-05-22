import random
import matplotlib.pyplot as plt
balance = 10000
deb = 100
i = 0
ready = []
while balance > 100 and i < 10000:
    clitinka = random.randint(1, 37)
    choice = random.randint(1, 37)
    if clitinka == choice:
        balance = balance + 36*deb 
    else:
        balance = balance - deb
    ready.append(balance)
    i += 1
iterations = list(range(1, len(ready) + 1))
plt.plot(iterations, ready, linestyle='-', color='blue')
plt.title("Зміна балансу після кожної гри")
plt.xlabel("Номер гри")
plt.ylabel("Баланс")
plt.grid(True)
plt.show()