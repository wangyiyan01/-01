import random
employeenumber=[x for x in range(1,301)]
third = []
second = []
first = []
for i in range(30):   #三等奖中奖人数
    n = random.choice(employeenumber)
    employeenumber.remove(n)
    third.append(n)
for i in range(6):    #二等奖中奖人数
    n = random.choice(employeenumber)
    employeenumber.remove(n)
    second.append(n)
for i in range(3):    #一等奖中奖人数
    n = random.choice(employeenumber)
    employeenumber.remove(n)
    first.append(n)

print("获得一等奖：泰国五日游的员工号码为:"," ".join(str(i) for i in first))
print("获得二等奖:iphone手机的员工号码为:"," ".join(str(i) for i in second))
print("获得三等奖:避孕套一盒的员工号码为:"," ".join(str(i) for i in third))

