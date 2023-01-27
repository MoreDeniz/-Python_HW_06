journal = {}
subject = ''
path = ''
# выбор класса для работы (файла)
def set_class(class_path: str):
    global path
    path = 'Class_Journal/' + class_path + '.txt'
# выбор учебного предмета
def set_subject(our_subject: str):
    global subject
    subject = our_subject

def open_file():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()

        for sub in file:
            if sub.split(';')[0] == subject:
                for study in sub.split(';')[1].strip().split(', '):
                    journal[study.split(':')[0]] = list(map(int, study.split(':')[1].split()))

# получаем журнал
def get_gournal():
    return journal

# табель успеваемости студента
def student_mark(student: str, mark: int):
    marks = list(journal.get(student))
    marks.append(mark)
    journal[student] = marks

def save_file():
    new_file = []
    print(journal)
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ':'.join(list(map(str, marks))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))

