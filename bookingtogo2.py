
def pickingNumbers(a):
    array = []
    for i in a:
        if i+1 in a:
            array.append(a.count(i)+a.count(i+1))
        else:
            array.append(a.count(i))
    
    print (max(array))

a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
b = [1, 2, 2, 3, 1, 2]
c = [4, 6, 5, 3, 3, 1]
pickingNumbers(a)
pickingNumbers(b)
pickingNumbers(c)
