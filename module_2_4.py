numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #создаем список

primes = [] #пустой список простых чисел
not_primes = [] #пустой список сложных чисел

for number in numbers:#записываем в переменную number зи списка
    if number == 1:#если number равна 1 то возращаесмя
        continue#возращаемся за следующем числом
    is_prime = True #иначе число не равно 1 (правда)
    for i in range(2, number):#пременная i берет значения в от 2 до числа переменной number
        if number % i == 0:#если number число делим на i(от 2 до number) и остаток =0
            is_prime = False # переменная лож(остаток 0)
            break #конец цикла
    if is_prime:#если переменная правда
        primes.append(number) #в список добавляем number
    else: #иначе
        not_primes.append(number) #в список добавляем number

print("Primes:", primes)#выводим список
print("Not Primes:", not_primes)#выводим список

