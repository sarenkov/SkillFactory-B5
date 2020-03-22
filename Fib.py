def Fib(count):
    sum = 2
    if count <= 3:
        print(*[x for x in range(1, count+1)])
    else:
        first, second = 1, 2
        print(first)
        print(second)

        for i in range(3, count + 1):
            third = first + second
            if third % 2 ==0:
                sum += third
            if third >= 4000000:
                break
            print(third)
            first, second = second, third

    print(sum)


if __name__ == '__main__':
    Fib(int(input('Введите число: ')))