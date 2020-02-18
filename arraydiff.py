import pdb

def array_diff(a, b):
    count = 0
    x = 0
    for i in a:
        for j in b:
            if a[count] == j:
                a[count] = 0
                x += 1
            else:
                continue
        count +=1

    for i in range(x):
        a.remove(0)



    return a
print(array_diff([1,3,3,2,6],[3]))