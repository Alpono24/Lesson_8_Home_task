
#1
# def apply_discount(product_price, discount):
#     final_price = product_price *(1 - discount)
#     assert 0 <= final_price <= product_price, 'Invalid final price'
#     return final_price
#
# print(apply_discount(100, 0.2))



#2

# # class MyException(Exception):
#     pass
#
# try:
#     number = int(input('Введите число: '))
#     if number == 10:
#         raise MyException ('10 no good')
#     result = 100 / number
#     # print(f'Результат: {result}')
#
# except ZeroDivisionError:
#     print('Ошибка ZO - ZeroDivisionError - деление на ноль')
# except ValueError:
#     print('Ошибка VE ValueError - не тот тип переменной')
# except MyException as my:
#     print(my)
# else:
#     print("Ok", result)
# finally:
#     print("Program finished")



def input_number():
    while True:
        try:
            num = int(input("Введите целое число: "))
            return num
        except ValueError:
            print("Ошибка ввода. Это не число. Попробуйте ещё раз.")

# Использование функции
number = input_number()
print(f"Введённое вами число: {number}")