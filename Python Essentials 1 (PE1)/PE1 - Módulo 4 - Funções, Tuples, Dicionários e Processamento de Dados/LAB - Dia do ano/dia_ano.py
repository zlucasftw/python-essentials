# LAB: Dia do ano: escrever e utilizar as suas próprias funções

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


def day_of_year(year, month, day):

    if year > 0 and (month > 0 and month <= 12) and (day > 0 and day <= 31):

        days = 0

        for month_year in range(month):

            month_year = days_in_month(year, month_year + 1)
            days += month_year

        return days

    else:
        return None


print(day_of_year(2000, 12, 31))
print(day_of_year(1900, 12, 31))
print(day_of_year(1900, 12, 32))
