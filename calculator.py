import sys


OPERATIONS = ['+', '-', '*', '/', 'q']


def choose_number():
    number = input('\nPlease enter number:\n(if you want to quit press q)\n')
    if number == 'q':
        sys.exit()
    while not number.isdigit():
        print('\nThis is not a number\n')
        number = input('\nPlease enter number:\n(if you want to quit press q)\n')
        if number == 'q':
            sys.exit()
    return int(number)


def addition(num_1, num_2):
    add_result = num_1 + num_2
    return add_result


def substraction(num_1, num_2):
    subst_result = num_1 - num_2
    return subst_result


def multiplication(num_1, num_2):
    multi_result = num_1 * num_2
    return multi_result


def division(num_1, num_2):
    div_result = num_1 / num_2
    return div_result


def choose_operation():
    operation = input('\nPlease enter operation (+, -, * or /):\n(if you want to quit press q)\n')
    while operation not in OPERATIONS:
        print('\nThis is not an operation\n')
        operation = input('\nPlease enter operation (+, -, * or /):\n(if you want to quit press q)\n')
    if operation == 'q':
        sys.exit()
    else:
        return operation


def calculation():
    num_1 = choose_number()
    oper = choose_operation()
    num_2 = choose_number()
    if oper == '+':
        add = addition(num_1, num_2)
        return add
    if oper == '-':
        sub = substraction(num_1, num_2)
        return sub
    if oper == '*':
        multi = multiplication(num_1, num_2)
        return multi
    if oper == '/':
        try:
            div = division(num_1, num_2)
        except ZeroDivisionError:
            print('Division by ZERO')
        return div


def main():
    stay = True
    while stay:
        result = calculation()

        print('\nResult: ' + str(result) + '\n')
        choose = input('\nIf you want to quit press q\n')
        if choose == 'q':
            stay = False
        else:
            continue

if __name__ == '__main__':
    main()
