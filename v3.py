n = int(input('Nechta odam kiritmoqchisiz: '))
lst = []
print('\n')
print("Ishchi ma'lumotini shu tartibda kiriting: ismi(Anvar) darajasi(Junior) maoshi(1000) bonus(200) bo'lim_raqami(1-bo'lim)")
print('\n')
for i in range(n) :
    lst.append(input("Ishchi ma'lumotlari: ").split(' '))
count = 0
count2 = 0
count3 = 0
for employee in lst :
    name,level,cash,bonus,mark = employee
    if int(bonus) > 0 :
        if int(mark[0]) == 1 :
            count+=1
        elif int(mark[0]) == 2 :
            count2+=1
        elif int(mark[0]) == 3 :
            count3+=1
    else :
        if int(mark[0]) == 1 :
            count-=1
        elif int(mark[0]) == 2 :
            count2-=1
        elif int(mark[0]) == 3 :
            count3-=1
if count > count2 > count3 :
    print("1-bo'lim")
elif count2 > count > count3 :
    print("2-bo'lim")
elif count3 > count2 > count :
    print("3-bo'lim")
elif count2 == count > count3 :
    print("1-bo'lim")
    print("2-bo'lim")
elif count2 == count3 > count :
    print("2-bo'lim")
    print("3-bo'lim")
elif count3 == count > count2 :
    print("1-bo'lim")
    print("3-bo'lim")
else :
    print("1-bo'lim")
    print("2-bo'lim")
    print("3-bo'lim")
    
 