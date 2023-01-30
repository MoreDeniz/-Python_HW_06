
import model

def input_class():
    print('Выберите класс: ')
    while True:
        try:
            choose_class = int(input('Введите порядковый номер:\n1 -> 7A\n2 -> 8B\t'))
            if choose_class == 1:
                print('7A')
                return '7A'
            elif choose_class == 2:
                print('8B')
                return '8B'
            else:
                print('Такого класса нет!')
        except:
            print('Надо ввести цифру!')

def input_subject():
    print('Выберите предмет: ')
    while True:
        try:
            choose_subj = int(input('Введите порядковый номер:\n1 -> математика\n'
                                    '2 -> русский\n3 -> география\n4 -> физкультура\t'))
            if choose_subj == 1:
                print('математика'.upper())
                return 'математика'
            elif choose_subj == 2:
                print('русский'.upper())
                return 'русский'
            elif choose_subj == 3:
                print('география'.upper())
                return 'география'
            elif choose_subj == 4:
                print('физкультура'.upper())
                return 'физкультура'
            else:
                print('Такого предмета нет!')
        except:
            print('Надо ввести цифру!')


def who_answer():
    print('Введите с большой буквы фамилию и имя из списка.')
    print('Если опрос окончен, введите 0.')
    while True:
        print('Кто будет отвечать? ')
        try:
            child = input()
            if child == '0':
                return 'exit'
            else:
                if model.journal.get(child):
                    print(child)
                    return child
                else:
                    print('Такого ученика нет!')
        except:
            print('Введите фамилию и имя или 0.')


def what_mark():
    while True:
        try:
           mark = input('Какая оценка? ')
           if 0 < int(mark) < 6:
               return str(mark)
           else:
               print('Такой оценки нет! Введите оценку от 1 до 5')
        except:
            print('Надо ввести цифру!')

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')


