data = [] #создание списка

print("Введите температуру:") #Ожидание данных от пользователя

data.append(float(input("Чуй: "))) #дополнение строки

data.append(float(input("Ош: ")))  #дополнение строки

data.append(float(input("Иссык-Куль: ")))  #дополнение строки

data.append(float(input("Талас: ")))  #дополнение строки

data.append(float(input("Жалал-Абад: ")))  #дополнение строки

data.append(float(input("Баткен: ")))  #дополнение строки

data.append(float(input("Нарын: ")))  #дополнение строки

#вычисление среднего показателя
print("\n\nСредний показатель температуры воздуха по КР на сегодня:" + str(round(sum(data) / 7, 2)))


