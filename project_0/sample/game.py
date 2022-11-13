import numpy as np


def random_predict(picked_num: int, bound: int) -> int:
    """Рандомно угадывает число

    Args:
        picked_num (int): Загаданное число.
        bound (int): Верхний предел диапазона допустимых чисел + 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, bound)  # предполагаемое число
        if picked_num == predict_number:
            break  # выход из цикла, если число угадано
    return count


def binary_search(picked_num: int, bound: int) -> int:
    """Угадывает число с помощью бинароного поиска

    Args:
        picked_num (int): Загаданное число.
        bound (int): Верхний предел диапазона допустимых чисел + 1.

    Returns:
        int: Число попыток
    """
    def tail_rec(low: int, high: int, attempts: int) -> int:
        mid = (low + high) // 2
        if (picked_num > mid):
            return tail_rec(mid, high, attempts + 1)
        else:
            if (picked_num < mid):
                return tail_rec(low, mid, attempts + 1)
            else:
                return attempts

    return tail_rec(0, bound, 0)


def score_game(predict_f) -> int:
    """За какое количство попыток в среднем за 1000 подходов алгоритм угадывает число от 1 до 100.

    Args:
        predict_f ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """

    count_ls = []
    random_array = np.random.randint(
        1, 101, size=(1000))  # список загаданных чисел

    for number in random_array:
        count_ls.append(predict_f(number, 101))

    score = int(np.mean(count_ls))

    print(
        f"Ваш алгоритм угадывает число в среднем за {score} попыт{'ку' if score % 10 == 1 else 'ки' if (score % 10 < 5 and score % 10 > 0) else 'ок'}")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_search)
