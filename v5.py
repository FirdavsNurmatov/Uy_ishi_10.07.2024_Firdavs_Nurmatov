n = int(input('list uzunligini kiriting: '))
lst = []
for i in range(n) :
    lst.append(input('naqsh rangini kiriting: '))
count = 0
lst = list(map(lambda x : x.lower(),lst))
for i in range(1,len(lst)) :
    if lst[i] != lst[i-1] :
        count+=1
x = len(lst)*2 + count
print(x)