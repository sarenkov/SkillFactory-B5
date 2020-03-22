def FizzBuzz(numbers_string):
    sum = 0
    if not numbers_string:
        print('Вы не ввели число. Давай досвиданья!')

    if type(numbers_string) is str:
        for number in (int(x) for x in numbers_string.split()):
            if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
                sum += number
                print('FizzBuzz')
            elif number % 5 == 0:
                sum += number
                print('Buzz')
            elif number % 3 == 0:
                sum += number
                print('Fizz')
            elif number % 7 ==0:
                sum += number
                print('Fizz7')
            else:
                continue
    else:
        for number in (x for x in numbers_string):
            if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
                sum += number
                print('FizzBuzz')
            elif number % 5 == 0:
                sum += number
                print('Buzz')
            elif number % 3 == 0:
                sum += number
                print('Fizz')
            elif number % 7 == 0:
                sum += number
                print('Fizz7')
            else:
                continue

    print(sum)

if __name__ == '__main__':
    # FizzBuzz(input('Введите числа через пробел: '))
    inp = tuple(x for x in range(1, 10000))
    FizzBuzz(inp)