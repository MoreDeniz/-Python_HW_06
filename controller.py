import view
import model

def start():
    model.set_class(view.input_class())
    # model.set_class(model.choose())
    model.set_subject(view.input_subject())
    model.open_file()
    student = ''
    while True:
        journal = model.get_gournal()
        view.list_of_child(journal)     # показываем журнал
        student = view.who_answer()     # кто отвечает
        if student == 'exit':
            break
        mark = int(view.what_mark())    # на какую оценку ответил
        model.student_mark(student, mark)   # занесли в журнал
    model.save_file()

