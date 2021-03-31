duration=int(input('Введите количество секунд: '))
minute=60
hour=3600
day=86400
# Если введённое время больше дня
if(duration>=day):
    in_day=duration//day
    duration=duration%day
    in_hour = duration // hour
    duration = duration % hour
    in_minute = duration // minute
    duration = duration % minute
    print(in_day,'Дн',in_hour,'час',in_minute,'мин',duration,'сек')
# В случае если введённое время меьше дня но больше часа
elif(duration>=hour):
    in_hour=duration//hour
    duration=duration%hour
    in_minute = duration // minute
    duration = duration % minute
    print(in_hour,'час',in_minute,'мин',duration,'сек')
# Время меньше часа но больше минуты
elif(duration>=minute):
    in_minute=duration//minute
    duration=duration%minute
    print(in_minute,'мин',duration,'сек')
else:
    print(duration,'сек')

