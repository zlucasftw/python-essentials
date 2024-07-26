# LAB: Quantos dias: escrever e usar as suas próprias funções

def is_year_leap(year):

    if year is None:
        return None

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):

    if year is None or month is None:
        return None

    if is_year_leap(year):

        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return months[month - 1]

    else:

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return months[month - 1]


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
