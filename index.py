# sum the same key values:
dic1 = {"k1":2,"k2":4,"k3":4}
dic2 = {"k3":7,"k4":8}
res = {}
for i,j in dic1.items():
    res[i] = j
for i,j in dic2.items():
    if i in res:
        res[i] = res[i] + j
    else:
        res[i] = j
print(res) 


name = "sandhya"
res3 = {}
for i in name:
    if i not in res3:
        res3[i] = 1
    else:
        res3[i] = res3[i] + 1
print(res3) 