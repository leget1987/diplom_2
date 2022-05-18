# Generated by Django 4.0.4 on 2022-05-18 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallSchedule',
            fields=[
                ('call_schedule_id', models.AutoField(db_column='id расписания звонков', primary_key=True, serialize=False, verbose_name='id расписания звонков')),
                ('class_start_time', models.TimeField(db_column='Время начала занятий', verbose_name='Время начала занятий')),
                ('class_stop_time', models.TimeField(db_column='Время окончания занятий', verbose_name='Время окончания занятий')),
            ],
            options={
                'verbose_name': 'Расписание звонка',
                'verbose_name_plural': 'Расписание звонков',
                'db_table': 'Расписание_звонка',
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('day_id', models.AutoField(db_column='id дня', primary_key=True, serialize=False, verbose_name='id дня')),
                ('name', models.CharField(db_column='Наименование', max_length=20, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'День',
                'verbose_name_plural': 'Дни',
                'db_table': 'День',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('discipline_id', models.AutoField(db_column='id предмета', primary_key=True, serialize=False, verbose_name='id предмета')),
                ('name', models.CharField(db_column='Наименование', max_length=50, verbose_name='Наименование')),
                ('cost', models.CharField(db_column='Стоимость', max_length=20, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'db_table': 'Предмет',
            },
        ),
        migrations.CreateModel(
            name='ListClasses',
            fields=[
                ('list_classes_id', models.AutoField(db_column='id списка классов', primary_key=True, serialize=False, verbose_name='id списка классов')),
            ],
            options={
                'verbose_name': 'Список класса',
                'verbose_name_plural': 'Списки классов',
                'db_table': 'Список_класса',
            },
        ),
        migrations.CreateModel(
            name='Offices',
            fields=[
                ('offices_id', models.AutoField(db_column='id кабинета', primary_key=True, serialize=False, verbose_name='id кабинета')),
                ('name', models.CharField(db_column='Наименование', max_length=50, verbose_name='Наименование')),
                ('capacity', models.CharField(db_column='Вместимость', max_length=20, verbose_name='Вместимость')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеты',
                'db_table': 'Кабинет',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('parent_id', models.AutoField(db_column='id родителя', primary_key=True, serialize=False, verbose_name='id родителя')),
                ('surname', models.CharField(db_column='Фамилия', max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(db_column='Имя', max_length=30, verbose_name='Имя')),
                ('patronymic', models.CharField(db_column='Отчество', max_length=30, verbose_name='Отчество')),
                ('phone_number', models.CharField(db_column='Номер телефона', max_length=20, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
                'db_table': 'Родитель',
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('quarter_id', models.AutoField(db_column='id четверти', primary_key=True, serialize=False, verbose_name='id четверти')),
                ('data_start_contract', models.DateField(db_column='Дата начала', verbose_name='Дата начала')),
                ('data_stop_contract', models.DateField(db_column='Дата конца', verbose_name='Дата конца')),
            ],
            options={
                'verbose_name': 'Четверть',
                'verbose_name_plural': 'Четверти',
                'db_table': 'Четверть',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_id', models.AutoField(db_column='id расписания', primary_key=True, serialize=False, verbose_name='id расписания')),
                ('start_start_period', models.DateField(db_column='Дата начала периода', verbose_name='Дата начала периода')),
                ('stop_period', models.DateField(db_column='Конец периода', verbose_name='Конец периода')),
                ('name', models.CharField(db_column='Наименование', max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
                'db_table': 'Расписание',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(db_column='id учителя', primary_key=True, serialize=False, verbose_name='id учителя')),
                ('surname', models.CharField(db_column='Фамилия', max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(db_column='Имя', max_length=30, verbose_name='Имя')),
                ('patronymic', models.CharField(db_column='Отчество', max_length=30, verbose_name='Отчество')),
                ('date_birth', models.DateField(db_column='Дата рождения', verbose_name='Дата рождения')),
                ('start_date_work', models.DateField(db_column='Дата начала работы', verbose_name='Дата начала работы')),
                ('phone_number', models.CharField(db_column='Телефон', max_length=20, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
                'db_table': 'Учитель',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year_id', models.AutoField(db_column='id года', primary_key=True, serialize=False, verbose_name='id года')),
                ('name', models.CharField(db_column='Наименование', max_length=20, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Год',
                'verbose_name_plural': 'Года',
                'db_table': 'Год',
            },
        ),
        migrations.CreateModel(
            name='TrainingClass',
            fields=[
                ('training_class_id', models.AutoField(db_column='id класса', primary_key=True, serialize=False, verbose_name='id класса')),
                ('name', models.CharField(db_column='Наименование', max_length=50, verbose_name='Наименование')),
                ('discipline', models.ForeignKey(db_column='id_предмета', on_delete=django.db.models.deletion.CASCADE, to='diplom.discipline', verbose_name='Предмет')),
                ('list_classes', models.ForeignKey(db_column='id_списка классов', on_delete=django.db.models.deletion.CASCADE, to='diplom.listclasses', verbose_name='Список классов')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
                'db_table': 'Класс',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(db_column='id ученика', primary_key=True, serialize=False, verbose_name='id ученика')),
                ('surname', models.CharField(db_column='Фамилия', max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(db_column='Имя', max_length=30, verbose_name='Имя')),
                ('patronymic', models.CharField(db_column='Отчество', max_length=30, verbose_name='Отчество')),
                ('date_birth', models.DateField(db_column='Дата рождения', verbose_name='Дата рождения')),
                ('parent', models.ForeignKey(db_column='id_родителя', on_delete=django.db.models.deletion.CASCADE, to='diplom.parent', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
                'db_table': 'Ученик',
            },
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('statement_id', models.AutoField(db_column='id заявления', primary_key=True, serialize=False, verbose_name='id заявления')),
                ('data_start_contract', models.DateField(db_column='Дата начала договора', verbose_name='Дата начала договора')),
                ('data_stop_contract', models.DateField(db_column='Дата окончания договора', verbose_name='Дата окончания договора')),
                ('lesson_type', models.BooleanField(db_column='Тип занятия', default=False, verbose_name='Тип занятия')),
                ('payment_status', models.BooleanField(db_column='Состояние оплаты', default=False, verbose_name='Состояние оплаты')),
                ('student', models.ForeignKey(db_column='id_ученика', on_delete=django.db.models.deletion.CASCADE, to='diplom.student', verbose_name='Ученик')),
            ],
            options={
                'verbose_name': 'Заявление',
                'verbose_name_plural': 'Заявлении',
                'db_table': 'Заявление',
            },
        ),
        migrations.CreateModel(
            name='RowTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bell', models.ForeignKey(db_column='id_звонока', on_delete=django.db.models.deletion.CASCADE, to='diplom.callschedule', verbose_name='Звонок')),
                ('day', models.ForeignKey(db_column='id_дня', on_delete=django.db.models.deletion.CASCADE, to='diplom.day', verbose_name='День')),
                ('office', models.ForeignKey(db_column='id_кабинета', on_delete=django.db.models.deletion.CASCADE, to='diplom.offices', verbose_name='Кабинет')),
                ('schedule', models.ForeignKey(db_column='id_расписания', on_delete=django.db.models.deletion.CASCADE, to='diplom.schedule', verbose_name='Расписание')),
                ('teacher', models.ForeignKey(db_column='id_учителя', on_delete=django.db.models.deletion.CASCADE, to='diplom.teacher', verbose_name='Учитель')),
                ('training_class', models.ForeignKey(db_column='id_класса', on_delete=django.db.models.deletion.CASCADE, to='diplom.trainingclass', verbose_name='Класс')),
            ],
            options={
                'db_table': 'Таблица строки',
            },
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('month_id', models.AutoField(db_column='id месяца', primary_key=True, serialize=False, verbose_name='id месяца')),
                ('name', models.CharField(db_column='Наименование', max_length=20, verbose_name='Наименование')),
                ('year', models.ForeignKey(db_column='id_года', on_delete=django.db.models.deletion.CASCADE, to='diplom.year', verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Месяц',
                'verbose_name_plural': 'Месяцы',
                'db_table': 'Месяц',
            },
        ),
        migrations.AddField(
            model_name='listclasses',
            name='statement',
            field=models.ForeignKey(db_column='id_заявления', on_delete=django.db.models.deletion.CASCADE, to='diplom.statement', verbose_name='Заявление'),
        ),
        migrations.AddField(
            model_name='day',
            name='month',
            field=models.ForeignKey(db_column='id_месяца', on_delete=django.db.models.deletion.CASCADE, to='diplom.month', verbose_name='Месяц'),
        ),
        migrations.CreateModel(
            name='AcademicPerformance',
            fields=[
                ('academic_performance_id', models.AutoField(db_column='id успеваемости', primary_key=True, serialize=False, verbose_name='id успеваемости')),
                ('estimation', models.CharField(db_column='Отметка', max_length=20, verbose_name='Отметка')),
                ('discipline', models.ForeignKey(db_column='id_предмета', on_delete=django.db.models.deletion.CASCADE, to='diplom.discipline', verbose_name='Предмет')),
                ('quarter', models.ForeignKey(db_column='id_четверти', on_delete=django.db.models.deletion.CASCADE, to='diplom.quarter', verbose_name='Четверть')),
                ('student', models.ForeignKey(db_column='id_ученика', on_delete=django.db.models.deletion.CASCADE, to='diplom.student', verbose_name='Ученик')),
                ('teacher', models.ForeignKey(db_column='id_чителя', on_delete=django.db.models.deletion.CASCADE, to='diplom.teacher', verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'Успеваемость',
                'verbose_name_plural': 'Успеваемости',
                'db_table': 'Успеваемость',
            },
        ),
    ]
