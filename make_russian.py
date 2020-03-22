def make_russian(number):
    number = str(number)
    if number.endswith('1') and not number.endswith('11'):
        return "{} студент".format(number)
    elif (number.endswith('2') or number.endswith('3') or number.endswith('4'))  and \
            not (number.endswith('12') or number.endswith('13') or number.endswith('14')):
        return "{} студента".format(number)
    else:
        return "{} студентов".format(number)



if __name__ == '__main__':
    # number = input('Введите число: ')
    for number in range (1002):
        print(f'{number} {make_russian(number)}')
