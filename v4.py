def my_sort(lst) :
    dct = {}
    for i in lst :
        count = 0
        for j in i :
            count = count + int(j)
        dct.setdefault(count,int(i))
    x = dict(sorted(dct.items()))
    answer = list(x.values())
    print(answer)

lst = []
try :
    n = int(input('nechta son kiritmoqchisiz:'))
    for i in range(n) :
        num = input('n=')
        if int(num) > 0 :
            lst.append(num)
        else :
            break
except :
    pass
else :
    my_sort(lst)