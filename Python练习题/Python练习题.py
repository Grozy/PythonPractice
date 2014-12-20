__author__ = 'sunguozhi'

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j)and(j!=k)and(k!=i):
                print(i,j,k)

money = 100000
getMoney = money * 0.1 #<= 10w
getMoney1 = getMoney + money * 0.075 # 10 <= 20w
getMoney2 = getMoney1 + 2 * money * 0.05  # 20 <= 40w
getMoney3 = getMoney2 + 2 * money * 0.03 # 40w <= 60w
getMoney4 = getMoney3 + 4 * money * 0.015 # 60w <= 100w
i = int(raw_input('input gain:\n'))

if i<= money:
    bouns = i * 0.1
elif i < 2 * money:
    bouns = getMoney + (i - money) * 0.075
elif i < 4 * money:
    bouns = getMoney1 + (i - 2 * money) * 0.05
elif i < 6 * money:
    bouns = getMoney2 + (i - 4 * money) * 0.03
elif i < 10 * money:
    bouns = getMoney3 + (i - 6 * money) * 0.015
elif i > 10 * money:
    bouns = getMoney4 + (i - 10 * money) * 0.01
print(bouns)

