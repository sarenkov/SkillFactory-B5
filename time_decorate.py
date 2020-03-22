from time import time


class Stopwatch:
    def __init__(self, func):
        self.func = func
        self.number_times = 5
        self.start_time = 0

    def __call__(self):
        self.start_time = time()
        for i in range(1, self.number_times + 1):
            print(f'Вызов функции №{i}')
            self.func()
        print(f'Время выполнения: {round(time() - self.start_time, 5)}')
        return self

    def __enter__(self):
        print('Начинаю замер времени выыполнения в контексте')
        self.__call__()
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    @Stopwatch  #Раскомментировать, если надо проверить работу Stopwatch как декоратора
    def printer():
        print('Снова запустил')
        for i in range(1, 110000000):
            pass


    printer() #Раскомментировать, если надо проверить работу Stopwatch как декоратора

    # Раскомментировать, если надо проверить работу контекстного менеджера
    # with Stopwatch(printer) as sw:
    #     pass
