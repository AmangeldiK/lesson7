while True:
    year = int(input('Enter year: '))
    def year_(year):
        if year % 4 != 0:
            print('This year is not a leap year')
        else:
            print('This year is a leap year')

    year_(year)
