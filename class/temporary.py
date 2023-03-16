class LessonItem:  # класс одного занятия (урока)
    def __init__(self, title: str, practices: int, duration: int):
        self.title=title
        self.practices=practices
        self.duration=duration


# ***magic!***

class Module:  # класс, описывающий один модуль (раздел) курса
    def __init__(self, name):
        self.name=name
        self.name=na

    def add_lesson(self,
                   lesson):  # добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);

    def remove_lesson(self, indx):  # удаление урока по индексу в списке lessons.


class Course:  # класс, отвечающий за управление курсом в целом:
    def __init__(self, name):
        self.na
        

    def add_module(self, module):  # добавление нового модуля в конце списка modules;

    def remove_module(self, indx):  # удаление модуля из списка modules по индексу в этом списке.