lst = []
n = int(input('list uzunligi = '))
for i in range(n) :
    lst.append(int(input('n=')))
for i in range(1,len(lst)) :
    if lst[i] < 0 > lst[i-1] or lst[i] > 0 < lst[i-1] :
        print(lst[i-1],lst[i])