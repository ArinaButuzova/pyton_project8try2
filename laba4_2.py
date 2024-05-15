def divide_100_by_number(number):
    try:
        result = 100 / number
        return result
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    

try:
    user_input = float(input("Введите число: "))
    print(divide_100_by_number(user_input))
except ValueError:
    print("Ошибка: введено не число")