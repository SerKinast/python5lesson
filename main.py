import os
import shutil

print('Консольный файловый менеджер')
while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только файлы')
    print('6. посмотреть только папки')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории (*необязательный пункт)')
    print('12. выход')

    choice = input('Выберите пункт меню: ')
    # Создать пааку
    if choice == '1':
        name = input('Введите название папки: ')
        if os.path.exists(name):
            print('Такая папка уже существует')
        else:
            os.mkdir(name)
    # Удалить папку
    elif choice == '2':
        name = input('Введите название папки: ')
        if os.path.exists(name):
            os.rmdir(name)
        else:
            print('Такой папки не существует')
    # Копировать файл
    elif choice == '3':
        old_name = input('Введите название копируемого файла: ')
        if os.path.exists(old_name):
            new_name = input('Введите название нового файла: ')
            old_path = str(os.getcwd() + '\\' + old_name)
            new_path = str(os.getcwd() + '\\' + new_name)
            shutil.copy(old_path, new_path)
        else:
            print('Такой папки не существует')
    # Просмотр содержимого рабочей директории
    elif choice == '4':
        print(str(os.getcwd()) + ':')
        for i in os.listdir():
            print(i)
    # Просмотреть только файлы рабочей директории
    elif choice == '5':
        objects = (os.listdir())
        for file in objects:
            path = str(os.getcwd()+ '\\' + file)
            if os.path.isfile(path):
                print(file)
    # Просмотреть только папки рабочей директории
    elif choice == '6':
        objects = (os.listdir())
        for folder in objects:
            path = str(os.getcwd() + '\\' + folder)
            if os.path.isdir(path):
                print(folder)
    # Просмотр информации об операционной системе
    elif choice == '7':
        import platform # "ос.юнэйм" некорректно работает на моей винде

        print(platform.uname())
    # Иноформация о создателе программы
    elif choice == '8':
        print()
        print('*' * 18)
        print('*' * 3, 'Created by', '*' * 3)
        print('*' * 3, 'Ser Kinast','*' * 3)
        print('*' * 18)
        print()
    # Играть в викторину "дни рождения политиков"
    elif choice == '9':
        from quiz import birth_victory
        birth_victory()
    # Открыть приложение "мой банковский счет"
    elif choice == '10':
        from console_apps import pocket
        pocket()
    # Смена рабочей директории
    elif choice == '11':
        path = input('Введите директорию, куда переходить: ')
        os.chdir(path)
    # Выход из программы
    elif choice == '12':
        break
