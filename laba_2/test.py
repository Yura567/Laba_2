enter = ""
list_a = []
while enter != "exit":
    enter = str(input("Виберіть ваіант 'A' чи 'B': "))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" \
            "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгдеєжзиіїйклмнопрстуфхцчшщьюя"
    if enter.upper() == "A" or enter.upper() == "А":
        a = input("Введіть текст: ").split()
        for i in a:
            if (i not in list_a) and len(i) > 3:
                list_a.append(i)
        list_a.sort()
        for x in range (0,len(list_a)):
            print(list_a[x])
        print("------------------")
    elif enter.upper() =="B" or enter.upper() == "Б":
        a = input("Введіть текст: ").split()
        for x in range(len(alphabet)):
            number = 0
            for i in a:
                number = number + i.count(alphabet[x])
            if number > 0:
                print(alphabet[x] + " - " + str(number))
        print("------------------")
