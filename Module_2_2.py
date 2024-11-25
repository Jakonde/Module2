first=int(input('введите первое число: '))
second=int(input('введите второе число: '))
third=int(input('введите третье число: '))
if first==second==third:
    print('3')
elif first==second:
    print('2')
elif first==third:
    print('2')
elif second==third:
    print('2')
else:
    print('0')
