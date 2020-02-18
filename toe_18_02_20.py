def divis(low, upp):
    x = []
    for i in range(low, upp):
        if i % 7 == 0 and i % 5 != 0:
            x.append(i)
    return x

def divis2(low, upp):
    return [x for x in range(low, upp) if x % 7 ==0 and x % 5 != 0]

print(divis2(2000,3200))