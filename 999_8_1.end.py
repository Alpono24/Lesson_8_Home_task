
print("1#__Исключения_____________________________************")

try:
    string = "Hello"
    number = int(string)
    print(number)
except ValueError:
    print("Была ошибка!")
print("Finish!")



print("")
print("2#___Исключения____________________________************")

try:
    string = "Hello"
    number = int(string)
    print(number)
except:
    print("Была ошибка _____dsds________ - не хороший вариант!")
print("Finish!")
print("")



print("3#_______________________________************")
def flow_ok():
    print("A: start")
    try:
        print("B: try-body")
        x = 1/0
        print("C: still in try")
    except ZeroDivisionError as e:
        print("D: except", type(e).__name__, e)
    print("E: after try/except")
flow_ok()




print("")
print("4#_Всплытие ошибок по стеку вызовов______________________________************")

def  inner():
    1/0

def outer_wrong():
    try:
        inner()
    except ValueError:
        print('VE')

def outer_right():
    try:
        inner()
    except ZeroDivisionError:
        print('ZE')

# outer_wrong()
outer_right()





print("")
print("5#_______________________________************")

# except (RuntimeError, TypeError, NameError, ZeroDivisionError)



print("")
print("6#__TRY_EXCEPTION___можно в одном блоке а можно по разным блокам___________________________************")
try:
    user_input  = input('Введите число: ')
    number = int(user_input)
    result = 100 / number
    print(f'Результат: {result}')
    d = {}
    d['a']
except (ZeroDivisionError):
    print('Ошибка ZO - ZeroDivisionError - деление на ноль')
except (ValueError):
    print('Ошибка VE ValueError - не тот тип переменной')
except Exception:
    print('Something went wrong!!!')





print("")
print("7#____БЛОК FINALLY___________________________************")

try:
    user_input  = input('Введите число: ')
    number = int(user_input)
    result = 100 / number
    print(f'Результат: {result}')

except (ZeroDivisionError):
    print('Ошибка ZO - ZeroDivisionError - деление на ноль')
except (ValueError):
    print('Ошибка VE ValueError - не тот тип переменной')
# except Exception:
#     print('Something went wrong!!!')
finally:
    print('it is ok - finally')




print("")
print("8#____БЛОК FINALLY___________________________************")
try:
    file = open('test.txt', 'w')
    file.write("Привет, Мир!")
    raise ValueError('raadsad')

except FileNotFoundError:
    print('FileNotFoundError')
except (ZeroDivisionError):
    print('Ошибка ZO - ZeroDivisionError - деление на ноль')
except (ValueError):
    print('Ошибка VE ValueError - не тот тип переменной')
finally:
    print('finally')
    file.close()




print("")
print("9#_Полная форма try except else finally______________________________************")
try:
    user_input  = input('Введите число: ')
    number = int(user_input)
    result = 100 / number
    print(f'Результат: {result}')
except (ZeroDivisionError):
    print('Ошибка ZO - ZeroDivisionError - деление на ноль')
except (ValueError):
    print('Ошибка VE ValueError - не тот тип переменной')
# except Exception:
#     print('Something went wrong!!!')
else:
    print(f'Finally {result}')
finally:
    print('end of programm!')



print("")
print("10#__!!!!!!!!!!!!_____________________________************")

import requests
url = "https://jsonplaceholder.typicode.com/posts/1"


try:
    session = requests.Session()
    response = session.get(url, timeout=5) ##Look at this info!!!
except requests.exceptions.Timeout:
    print('It is all right, but it is except - Error, server dont answer!!!')
except requests.exceptions.ConnectionError:
    print('It is all right, but it is except - Error, doesnt connection!!!')
else:
    print('It is all right!!!')
    print(response.json())
finally:
    print('Blok finally')
    session.close()

print("")
print("")
print("11#___Иерархия исключений_____Иерархия исключений_______Иерархия исключений________________************")
try:
    number = int(input("Enter a number: "))
    print("Entered number is:", number)
except ValueError as e:
    print("Info about exception", e)
print("End of program!")


print("")
print("")
print("12#__RAISE__RAISE__RAISE__RAISE__RAISE__RAISE__RAISE__RAISE__RAISE__RAISE__RAISE__RAISE__RAISE_____************")

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# try:
#     if b == 0:
#         raise ValueError('ZeroDivisionError')
# except ValueError:

print("")
print("")
print("12# Assertions Assertions Assertions Assertions")
#
# def sqrt(x):
#     assert x >= 0, 'forbidden'
#     return x ** (1 / 2)
# print("SQRT :", sqrt(-1))


print("")
print("")
print("13# Assertions Assertions Assertions Assertions")

def apply_discount(product_price, discount):
    final_price = product_price *(1 -  discount)
    assert 0 <= final_price <= product_price, "Invalid final price"
    return final_price

print(apply_discount(100, 0.2))

print("")
print("")
print("14# ----------------------------------->")

