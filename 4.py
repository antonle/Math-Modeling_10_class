day = 15
month = 10
year = 2019
if (month == 10) or (month == 1):
    a = 1
elif month == 5:
    a = 2
elif month == 8:
    a = 3
elif (month == 2) or (month == 3) or (month == 11):
    a = 4
elif month == 6:
    a = 5
elif (month == 12) or (month == 9):
    a = 6
else:
    a = 0
b = (6 + year%100 + (year%100)//4)%7
s = (day + a + b)%7
if s==0:
    print('воскресенье')
elif s==1:
    print('суббота')
elif s==2:
    print('понедельник')
elif s==3:
    print('вторник')
elif s==4:
    print('среда')
elif s==5:
    print('четверг')
else:
    print('пятница')
