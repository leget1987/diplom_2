from django.db import models


# Create your models here.
class Quarter(models.Model):
    # четверть
    quarter_id = models.AutoField(primary_key=True, db_column="id четверти", verbose_name="id четверти")
    data_start_contract = models.DateField(db_column="Дата начала", verbose_name="Дата начала")
    data_stop_contract = models.DateField(db_column="Дата конца", verbose_name="Дата конца")

    def __str__(self):
        return f'Четверть {self.data_start_contract} - {self.data_stop_contract}'

    class Meta:
        db_table = 'Четверть'
        verbose_name = 'Четверть'
        verbose_name_plural = 'Четверти'


class AcademicPerformance(models.Model):
    # успеваемость
    academic_performance_id = models.AutoField(primary_key=True, db_column="id успеваемости",
                                               verbose_name="id успеваемости")
    student = models.ForeignKey(to='Student', on_delete=models.CASCADE, db_column="id_ученика", verbose_name="Ученик")
    quarter = models.ForeignKey(to='Quarter', on_delete=models.CASCADE, db_column="id_четверти",
                                verbose_name="Четверть")
    discipline = models.ForeignKey(to='Discipline', on_delete=models.CASCADE, db_column="id_предмета",
                                   verbose_name="Предмет")
    teacher = models.ForeignKey(to='Teacher', on_delete=models.CASCADE, db_column="id_чителя", verbose_name="Учитель")
    estimation = models.CharField(max_length=20, db_column="Отметка", verbose_name="Отметка")

    def __str__(self):
        return f"Успеваемость {self.student} по предмету {self.discipline}"

    class Meta:
        db_table = 'Успеваемость'
        verbose_name = 'Успеваемость'
        verbose_name_plural = 'Успеваемости'


class Student(models.Model):
    # ученик
    student_id = models.AutoField(primary_key=True, db_column="id ученика", verbose_name="id ученика")
    parent = models.ForeignKey(to='Parent', on_delete=models.CASCADE, db_column="id_родителя", verbose_name="Родитель")
    surname = models.CharField(max_length=30, db_column="Фамилия", verbose_name="Фамилия")
    first_name = models.CharField(max_length=30, db_column="Имя", verbose_name="Имя")
    patronymic = models.CharField(max_length=30, db_column="Отчество", verbose_name="Отчество")
    date_birth = models.DateField(db_column="Дата рождения", verbose_name="Дата рождения")

    def __str__(self):
        return f'Ученик {self.surname}'

    class Meta:
        db_table = 'Ученик'
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class Parent(models.Model):
    # родитель
    parent_id = models.AutoField(primary_key=True, db_column="id родителя", verbose_name="id родителя")
    surname = models.CharField(max_length=30, db_column="Фамилия", verbose_name="Фамилия")
    first_name = models.CharField(max_length=30, db_column="Имя", verbose_name="Имя")
    patronymic = models.CharField(max_length=30, db_column="Отчество", verbose_name="Отчество")
    phone_number = models.CharField(max_length=20, db_column="Номер телефона", verbose_name="Номер телефона")

    def __str__(self):
        return f'Родитель {self.surname}'

    class Meta:
        db_table = 'Родитель'
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'


class Statement(models.Model):
    # заявление
    statement_id = models.AutoField(primary_key=True, db_column="id заявления", verbose_name="id заявления")
    student = models.ForeignKey(to='Student', on_delete=models.CASCADE, db_column="id_ученика", verbose_name="Ученик")
    data_start_contract = models.DateField(db_column="Дата начала договора", verbose_name="Дата начала договора")
    data_stop_contract = models.DateField(db_column="Дата окончания договора", verbose_name="Дата окончания договора")
    lesson_type = models.BooleanField(default=False, db_column="Тип занятия", verbose_name="Тип занятия")
    payment_status = models.BooleanField(default=False, db_column="Состояние оплаты", verbose_name="Состояние оплаты")

    def __str__(self):
        return f'Заявление от {self.student}'

    class Meta:
        db_table = 'Заявление'
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявлении'


class Teacher(models.Model):
    # учитель
    teacher_id = models.AutoField(primary_key=True, db_column="id учителя", verbose_name="id учителя")
    surname = models.CharField(max_length=30, db_column="Фамилия", verbose_name="Фамилия")
    first_name = models.CharField(max_length=30, db_column="Имя", verbose_name="Имя")
    patronymic = models.CharField(max_length=30, db_column="Отчество", verbose_name="Отчество")
    date_birth = models.DateField(db_column="Дата рождения", verbose_name="Дата рождения")
    start_date_work = models.DateField(db_column="Дата начала работы", verbose_name="Дата начала работы")
    phone_number = models.CharField(max_length=20, db_column="Телефон", verbose_name="Телефон")

    def __str__(self):
        return f'Учитель {self.surname}'

    class Meta:
        db_table = 'Учитель'
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Year(models.Model):
    year_id = models.AutoField(primary_key=True, db_column="id года", verbose_name="id года")
    name = models.CharField(max_length=20, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return f'Год {self.name}'

    class Meta:
        db_table = 'Год'
        verbose_name = 'Год'
        verbose_name_plural = 'Года'


class Month(models.Model):
    month_id = models.AutoField(primary_key=True, db_column="id месяца", verbose_name="id месяца")
    year = models.ForeignKey(to='Year', on_delete=models.CASCADE, db_column="id_года", verbose_name="Год")
    name = models.CharField(max_length=20, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return f'Месяц {self.name}'

    class Meta:
        db_table = 'Месяц'
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'


class Day(models.Model):
    day_id = models.AutoField(primary_key=True, db_column="id дня", verbose_name="id дня")
    month = models.ForeignKey(to='Month', on_delete=models.CASCADE, db_column="id_месяца", verbose_name="Месяц")
    name = models.CharField(max_length=20, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return f'День {self.name}'

    class Meta:
        db_table = 'День'
        verbose_name = 'День'
        verbose_name_plural = 'Дни'


class Offices(models.Model):
    # кабинеты
    offices_id = models.AutoField(primary_key=True, db_column="id кабинета", verbose_name="id кабинета")
    name = models.CharField(max_length=50, db_column="Наименование", verbose_name="Наименование")
    capacity = models.CharField(max_length=20, db_column="Вместимость", verbose_name="Вместимость")

    def __str__(self):
        return f'Кабинет {self.name}'

    class Meta:
        db_table = 'Кабинет'
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'


class RowTable(models.Model):
    schedule = models.ForeignKey(to='Schedule', on_delete=models.CASCADE, db_column="id_расписания",
                                 verbose_name="Расписание")
    training_class = models.ForeignKey(to='TrainingClass', on_delete=models.CASCADE, db_column="id_класса",
                                       verbose_name="Класс")
    teacher = models.ForeignKey(to='Teacher', on_delete=models.CASCADE, db_column="id_учителя", verbose_name="Учитель")
    day = models.ForeignKey(to='Day', on_delete=models.CASCADE, db_column="id_дня", verbose_name="День")
    bell = models.ForeignKey(to='CallSchedule', on_delete=models.CASCADE, db_column="id_звонока", verbose_name="Звонок")
    office = models.ForeignKey(to='Offices', on_delete=models.CASCADE, db_column="id_кабинета", verbose_name="Кабинет")

    class Meta:
        db_table = 'Таблица строки'


class CallSchedule(models.Model):
    call_schedule_id = models.AutoField(primary_key=True, db_column="id расписания звонков",
                                        verbose_name="id расписания звонков")
    class_start_time = models.TimeField(db_column="Время начала занятий", verbose_name="Время начала занятий")
    class_stop_time = models.TimeField(db_column="Время окончания занятий", verbose_name="Время окончания занятий")

    def __str__(self):
        return f'Расписание звонка'

    class Meta:
        db_table = 'Расписание_звонка'
        verbose_name = 'Расписание звонка'
        verbose_name_plural = 'Расписание звонков'


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True, db_column="id расписания", verbose_name="id расписания")
    start_start_period = models.DateField(db_column="Дата начала периода", verbose_name="Дата начала периода")
    stop_period = models.DateField(db_column="Конец периода", verbose_name="Конец периода")
    name = models.CharField(max_length=50, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return f'Расписание {self.name}'

    class Meta:
        db_table = 'Расписание'
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class Discipline(models.Model):
    discipline_id = models.AutoField(primary_key=True, db_column="id предмета", verbose_name="id предмета")
    name = models.CharField(max_length=50, db_column="Наименование", verbose_name="Наименование")
    cost = models.CharField(max_length=20, db_column="Стоимость", verbose_name="Стоимость")

    def __str__(self):
        return f'Предмет {self.name}'

    class Meta:
        db_table = 'Предмет'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class TrainingClass(models.Model):
    training_class_id = models.AutoField(primary_key=True, db_column="id класса", verbose_name="id класса")
    discipline = models.ForeignKey(to='Discipline', on_delete=models.CASCADE, db_column="id_предмета",
                                   verbose_name="Предмет")
    # list_classes = models.ForeignKey(to='ListClasses', on_delete=models.CASCADE, db_column="id_списка классов",
    #                                  verbose_name="Список классов")
    name = models.CharField(max_length=50, db_column="Наименование", verbose_name="Наименование")

    def __str__(self):
        return f'Класс {self.name}'

    class Meta:
        db_table = 'Класс'
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class ListClasses(models.Model):
    list_classes_id = models.AutoField(primary_key=True, db_column="id списка классов", verbose_name="id списка "
                                                                                                     "классов")
    statement = models.ForeignKey(to='Statement', on_delete=models.CASCADE, db_column="id_заявления",
                                  verbose_name="Заявление")
    training_class = models.ForeignKey(to='TrainingClass', on_delete=models.CASCADE, db_column="id_класса",
                                     verbose_name="Список классов", default='')

    def __str__(self):
        return f'Список классов'

    class Meta:
        db_table = 'Список_класса'
        verbose_name = 'Список класса'
        verbose_name_plural = 'Списки классов'
