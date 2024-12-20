from random import randint
n = randint (0, 12)
i=1
print("я заагдал число от 1 до 12. Попробуй его угадать, у тебя всего 3 попытки")
while i <=3:
    u = int(input(str(i) + '-я ппытка: '))
    if u > n:
        print ('Много')
        print ("Но тепло" if abs(n-u) <=2 else "И холодно")
    elif u < n:
        print('Мало')
        print("Но тепло" if abs(n-u) <=2 else "И холодно")
    else:
        print('Вы угадали число с  %d-й, поздравляю!' % i)
        break
    i += 1
else:
    print("Вы не угадали число", n)