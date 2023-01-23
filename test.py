import os
the_start = 1
while the_start == 1:
    more = input('Если хотите начать сначала, напишите "Да": ')
    if more == 'Да' or 'да':
        the_start = 1
    else:
        the_start = 0

# p = os.path.basename(\python\python5lesson)
# print(type(os.path.abspath()))
# print(os.listdir(\Обучение\python\python5lesson))