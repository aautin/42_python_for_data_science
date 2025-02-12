import datetime as dt


def get_seconds_difference(past: dt.datetime, today: dt.datetime):
    time_difference = today - past
    days = time_difference.days
    seconds = time_difference.seconds
    microseconds = time_difference.microseconds
    return (days * 24 * 3600) + seconds + (microseconds / 1000)


def main():
    time_difference = get_seconds_difference(
        dt.datetime(1970, 1, 1), dt.datetime.today())
    print("Seconds since January 1, 1970:",
          f"{time_difference:,}",
          "or",
          f"{time_difference:.2e}",
          "in scientific notation")

    # def month_in_str(month):
    #     months = {
    #         1 : "Jan", 2 : "Feb", 3 : "Mar",
    #         4 : "Apr", 5 : "Mai", 6 : "Jun",
    #         7 : "Jul", 8 : "Aug", 9 : "Sep",
    #         10 : "Oct", 11 : "Nov", 12 : "Dec"
    #     }
    #     return months[month]
    # today = dt.datetime.today()
    # print(month_in_str(today.month), today.day, today.year)
    print(dt.datetime.strftime(dt.datetime.today(), "%b"),
          dt.datetime.today().day,
          dt.datetime.today().year)


main()
