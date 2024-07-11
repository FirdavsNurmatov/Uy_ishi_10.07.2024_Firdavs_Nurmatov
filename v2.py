dct = {}
n = int(input('list uzuligini kiritng: '))
count = 0
count2 = 0
lst = []
lst2 = []
for i in range(n) :
    name = input("name: ")
    num = int(input('1 or 0: '))
    dct.setdefault(name,num)
    if num == 1 :
        count+=1
        lst.append(name)
    elif num == 0 :
        count2+=1
        lst2.append(name)
if count > count2 :
    x = ' '.join(lst)
    print("Anwer:")
    print(1,'\n',x)
elif count2 > count :
    x = ' '.join(lst2)
    print("Anwer:")
    print(0,'\n',x)
else :
    x = ' '.join(lst)
    y = ' '.join(lst2)
    print("Anwer:")
    print(0,'\n',y,'\n',1,'\n',x)