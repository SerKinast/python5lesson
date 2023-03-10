import random

def birth_victory():
    birthdays = {'Путин': '07.10.1952',
                 'Лавров': '21.03.1950',
                 'Небензя': '26.02.1962',
                 'Шойгу': '21.04.1955',
                 'Володин': '04.02.1964',
                 'Голикова': '09.02.1966',
                 'Медведев': '14.09.1965',
                 'Жириновский': '25.04.1946',
                 'Матвиенко': '07.04.1949',
                 'Гладков': '15.01.1969'
                 }

    writing_birthdays = {'07.10.1952': 'седьмого октября 1952 года',
                         '21.03.1950': 'двадцать первого марта 1950 года',
                         '26.02.1962': 'двадцать шестого февраля 1962 года',
                         '21.04.1955': 'двадцать первого апреля 1955 года',
                         '04.02.1964': 'четвертого февраля 1964 года',
                         '09.02.1966': 'девятого февраля 1966 года',
                         '14.09.1965': 'четырнадцатого сентября 1965 года',
                         '25.04.1946': 'двадцать пятого апреля 1946 года',
                         '07.04.1949': 'седьмого апреля 1949 года',
                         '15.01.1969': 'пятнадцатого января 1969 года'
                         }

    # the_start = 1
    # while the_start == 1:

    points = 0
    faults = 0
    count = int(input('Введите количество вопросов: '))
    steps = [i for i in range(0, count)]
    for step in steps:
        surname, birthday = random.choice(list(birthdays.items()))
        print('Когда родился ', surname, '?')
        answer = input('Формат даты дд.мм.гггг')
        if birthday == answer:
            print('Верно!')
            points += 1
        else:
            print('Не верно! ', writing_birthdays[birthday])
            faults += 1

    share = points * 100 / 5
    print('Верных ответов:', points)
    print('Неверных ответов:', faults)
    print('Доля верных ответов:', share, '%')

    #     more = input('Если хотите начать сначала, напишите "Да": ')
    #
    # if more == 'Да' or 'да':
    #     the_start = 1
    # else:
    #     the_start = 0
    # return points
    # return faults
    # return share

