print("Lesson 8. Home task №2. Ver. 2 (с использованием dict и lambda-функций)")
"""
2. Реализовать программу с функционалом калькулятора для
операций над двумя числами. Числа и операция вводятся
пользователем с клавиатуры. Использовать ООП.
Использовать обработку исключений
"""
print(" ")


def calc_for_two_values():
    while True:

        class MissingAction(Exception):
            pass

        try:
                actions = {
                "+": lambda number_1, number_2: number_1 + number_2,
                "-": lambda number_1, number_2: number_1 - number_2,
                "*": lambda number_1, number_2: number_1 * number_2,
                "/": lambda number_1, number_2: number_1 / number_2 if number_2 != 0 else None,
                "//": lambda number_1, number_2: number_1 // number_2,
                "%": lambda number_1, number_2: number_1 % number_2,
                }
                number_1 = float(input("Введите первое число a:  "))
                number_2 = float(input("Введите второе число b:  "))
                action = input("Введите действие необходимое для выполнения над двумя числами: ")
                if action == "+" or action == "-" or action == "*"or action == "/"or action == "//"or action == "%":
                    res = actions[action](number_1, number_2)
                else:
                    raise MissingAction('Действие которое вы ввели недопустимо в данной программе.')

                if number_2 == 0:
                    raise ZeroDivisionError

        except ValueError:
            print("""Ошибка. Вы ввели не число. Повторите ввод данных.""")
        except ZeroDivisionError:
            print("""Ошибка. Делить на ноль "нельзя", т.к. это не укладывается в общепринятые аксиомы работы с числами, а говоря проще - потому что люди так договорились.
            Если "передоговориться", т.е. выбрать другой набор аксиом - на ноль будет можно делить, но много привычных теорем перестанут быть корректными, 
            а значит и результаты таких вычислений не получится применять на практике.""")
        except MissingAction as my:
            print(my)
        else:
                print(f"Итого выполнения: res = {number_1}{action}{number_2} = {res} ")
                print("")
                print("Программа выполнила код без исключений.")

        finally:
                print("Программа завершила работу!")

calc_for_two_values()
