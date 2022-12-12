salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

i = 0
while i <= months-1:
    money_capital += spend - salary   #Суммируем разницу между расходами и зарплатой
    spend *= 1.03                        #Увеличиваем расходы на 3%
    i += 1


print(round(money_capital))
