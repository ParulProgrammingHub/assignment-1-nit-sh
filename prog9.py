m1 = int(input('Enter marks of 1 : '))
m2 = int(input('Enter marks of 2 : '))
m3 = int(input('Enter marks of 3 : '))
m4 = int(input('Enter marks of 4 : '))
m5 = int(input('Enter marks of 5 : '))
perc = (m1+m2+m3+m4+m5)*100/500
if perc<35 :
    print('Student has Failed!!!!, with percentage of',perc)
else :
    print('Student has PAssedd!!!, with percentage of',perc)
