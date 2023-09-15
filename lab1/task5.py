from scipy.stats import binom

people_count = 1000
p_ten_in_row = 2 * (0.5 ** 10)


def calc_first():
    p_no_one_has_ten_in_row = (1 - p_ten_in_row) ** people_count
    return 1 - p_no_one_has_ten_in_row


def calc_second():
    # 1) xyyyyyyyyx
    # 2) xxyyyyyyyy
    # 3) yxyyyyyyyy
    # 4) yyyyyyyyxy
    # 5) yyyyyyyyxx
    # и еще 5 наоборот => всего 10 интересующих комбинаций
    all_combs = 2 ** 10
    p_get_exactly_eight_in_row = 10 / all_combs
    return 1 - (1 - p_get_exactly_eight_in_row) ** 1000


def calc_third():
    k = 3  # нужное число успехов
    n = 1000  # "количество экспериментов" (количество людей)
    return binom.pmf(k, n, p_ten_in_row)


print(f"First answer: {calc_first()}")
print(f"Second answer: {calc_second()}")
print(f"Third answer: {calc_third()}")
