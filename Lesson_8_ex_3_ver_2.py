print("Lesson 8. Home task №3***. Ver_2")

print(" ")

"""
Логирование не добавлено 
4*. 
Добавить собственное исключение UnsupportedOperationError, которое выбрасывается, если встречается операция,
отличная от + - * /.
Добавить логирование всех ошибок в отдельный файл errors.log с указанием времени и строки, вызвавшей ошибку.
"""


class UnsupportedOperationError(Exception):
    """
    Добавить собственное исключение UnsupportedOperationError,
    которое выбрасывается, если встречается операция, отличная от + - * /.
    """
    pass


try:
    file = open("input.txt", "r", encoding="utf-8")
    res = open("output.txt", "w", encoding="utf-8")

    for line in file:
            try:
                numbers_for_actions = line.strip().split()
                number_1 = float(numbers_for_actions[0])
                action = numbers_for_actions[1]
                number_2 = float(numbers_for_actions[2])

                if action == "+" or action == "-" or action == "*" or action == "/":
                    if action == '+':
                        result = number_1 + number_2
                        print(line.rstrip() + " = " + str(result))             # Вывод в консоль
                        res.write(line.rstrip() + " = " + str(result) + "\n")  # Вывод в файл
                    elif action == '-':
                        result = number_1 - number_2
                        print(line.rstrip() + " = " + str(result))             # Вывод в консоль
                        res.write(line.rstrip() + " = " + str(result) + "\n")  # Вывод в файл
                    elif action == '*':
                        result = number_1 * number_2
                        print(line.rstrip() + " = " + str(result))             # Вывод в консоль
                        res.write(line.rstrip() + " = " + str(result) + "\n")  # Вывод в файл
                    elif action == '/':
                        result = number_1 / number_2
                        print(line.rstrip() + " = " + str(result))             # Вывод в консоль
                        res.write(line.rstrip() + " = " + str(result) + "\n")  # Вывод в файл

                else:
                    raise UnsupportedOperationError('Неверный оператор - Действие которое вы ввели недопустимо в данной программе.')

            except ZeroDivisionError:
                res.write(line.rstrip() + " = Ошибка: деление на ноль."+ "\n")   #Вывод в файл
                print(line.rstrip() + " = Ошибка: деление на ноль.")             #Вывод в консоль
            except UnsupportedOperationError as uoe:
                res.write(line.rstrip() + " = Неверный оператор - Действие которое вы ввели недопустимо в данной программе." + "\n")  # Вывод в файл
                print(uoe)                                                      #Вывод в консоль
            except (ValueError, NameError):
                res.write(line.rstrip()+ " = Ошибка: некорректные данные." + "\n") #Вывод в файл
                print(line.rstrip() + " = Ошибка: некорректные данные.")           #Вывод в консоль
            except Exception:
                res.write(line.rstrip() + " = Неизвестная ошибка." + "\n")         #Вывод в файл
                print(line.rstrip() + " = Неизвестная ошибка.")                    #Вывод в консоль

except FileNotFoundError:
    print("Невозможно открыть файл.")
except SyntaxError:
    print("Ошибка при работе с файлом.")
finally:
    print(" ")
    print("Программа завершила работу.")
    file.close()
    res.close()
    print(f"Файл для чтения закрыт? (если True, то закрыт): ",file.closed)
    print(f"Файл для записи закрыт? (если True, то закрыт): ",res.closed)











"""
1. Есть текстовый файл input.txt, в котором построчно записаны арифметические операции, например:
10 / 2
5 * 7
8 - 3
9 / 0
hello + 5
12 / 4

2 . Нужно написать программу, которая:
читает файл построчно;
пытается выполнить каждую операцию;
обрабатывает возможные исключения:
- ZeroDivisionError → вместо результата писать "Ошибка: деление на ноль"
- ValueError / TypeError → "Ошибка: некорректные данные"
- любое другое исключение → "Неизвестная ошибка"

3. записывает результаты в новый файл output.txt в формате:
10 / 2 = 5.0
5 * 7 = 35
8 - 3 = 5
9 / 0 = Ошибка: деление на ноль
hello + 5 = Ошибка: некорректные данные
12 / 4 = 3.0

4*. Добавить собственное исключение UnsupportedOperationError, которое выбрасывается, 
если встречается операция,
отличная от + - * /.
Добавить логирование всех ошибок в отдельный файл errors.log с указанием времени и строки, 
вызвавшей ошибку.
"""

