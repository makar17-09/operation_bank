from random import randint
print("проект 'банк'")
x = int(input("введите ваш возраст  "))
sum = 10000
if x >= 18 and x < 90:
    s = int(input("введите номер ячейки банка   "))
    if s >= 0 and s <= 276:
        d = input("какую операцию хотите сделать? ").lower()
        Y = randint(1,2)
        if d == "вывод":
            c = int(input("введите пин код "))
            if c == 2375:
                print("пин код верный ")
                F = int(input("какую сумму вы хотите снять? "))
                if sum - F >= 0:
                    sum = sum - F
                    print("успешно")
                    G = input("хотите узнать ваш баланс?  ")
                    if G == "да" or G == "конечно" or G == "почему бы и нет":
                        print(sum)
                else:
                    print("упс... не хватает средств")
                    G = input("хотите узнать ваш баланс?  ")
                    if G == "да" or G == "конечно" or G == "почему бы и нет":
                        print(sum)
            else:
                print("пин код не верный")
        elif d == 'ввод':
            c = int(input("введите пин код "))
            if c == 2375:
                print("пин код верный ")
                f = int(input("какую сумму вы хотите внести? "))
                sum = sum + f
                print("успешно, вы что миллионер?")
                g = input("хотите узнать ваш баланс?  ")
                if g == "да" or g == "конечно" or g == "почему бы и нет":
                    print(sum)
                else:
                    print("?????????????")
            else:
                print("неверный пин код ")
        elif d == "z".lower() or d == "это ограбление" and Y == 1:
            print("л л ладно толькок не бейте ппожаллуййста")
            sum = sum + 100000
            print(sum, "и 5 звезд от ограбления")
            print("что , КОПЫ")
            r = input("за вами полиция ваши действия?")
            if r == "пиу пиу":
                print("bambini di banco")
                print("вау вы успешно ограбели банк")
            elif r == "бежать":
                print("addios bambini")
                print("вау вы успешно ограбели банк")
            elif r == "сдаться":
                print("maledetti poliziotti")
        elif d == "z".lower() or d == "это ограбление" and Y == 2:
            u = randint(0,5)
            if u == 1 :
                print("вы подскользнулись на кожуре банана, летальный исход")
            elif u == 2:
                print("вас прибанковали к банку,банкир, летальный исход")
            elif u == 3:
                print("на вас набросился карате-хомяк,летальный исход")
            elif u == 4:
                print("вы подавились лазерно-космической мухой-киборгом")
            elif u == 5:
                print("вас засосало в унитаз")
        else:
            print("данной команды не существует")
    else:
        print("данной ячейки не существует")
else:
    print("доступ запрещен")
