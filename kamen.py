print('Сыграем в игру камень ножницы или бумага')
a = str(input("Введите камень, ножницы или бумага: "))
b = str(input("Введите камень, ножницы или бумага: "))
if a == 'ножницы' and b == 'бумага':
    print('Победили  ножницы')
elif a == 'камень' and b == 'бумага':
    print('Победили  бумага')
elif a == 'бумага' and b == 'камень':
    print('Победили  бумага')
elif a == 'камень' and b == 'ножницы':
    print('Победили  бумага')
elif a == b:
    print('Ничья')
else:
    print('Вы не соответствуете')