from django.contrib import admin
from .models import *


# Register your models here.
class QuarterView(admin.ModelAdmin):
    list_display = ('data_start_contract', 'data_stop_contract')


class AcademicPerformanceView(admin.ModelAdmin):
    list_display = ('student', 'quarter', 'discipline', 'teacher', 'estimation')


class StudentView(admin.ModelAdmin):
    list_display = ('surname', 'first_name', 'patronymic', 'parent', 'date_birth')


class ParentView(admin.ModelAdmin):
    list_display = ('surname', 'first_name', 'patronymic', 'phone_number')


class StatementView(admin.ModelAdmin):
    list_display = ('student', 'data_start_contract', 'data_stop_contract', 'lesson_type', 'payment_status')


class TeacherView(admin.ModelAdmin):
    list_display = ('surname', 'first_name', 'patronymic', 'date_birth', 'start_date_work', 'phone_number')


class YearView(admin.ModelAdmin):
    list_display = ('name',)


class MonthView(admin.ModelAdmin):
    list_display = ('name',)


class DayView(admin.ModelAdmin):
    list_display = ('name',)


class OfficesView(admin.ModelAdmin):
    list_display = ('name', 'capacity')


class CallScheduleView(admin.ModelAdmin):
    list_display = ('class_start_time', 'class_stop_time')


class ScheduleView(admin.ModelAdmin):
    list_display = ('start_start_period', 'stop_period', 'name',)


class DisciplineView(admin.ModelAdmin):
    list_display = ('name', 'cost')


class TrainingClassView(admin.ModelAdmin):
    list_display = ('discipline', 'name')


class ListClassesView(admin.ModelAdmin):
    list_display = ('statement', 'training_class')


admin.site.register(Quarter, QuarterView)
admin.site.register(AcademicPerformance, AcademicPerformanceView)
admin.site.register(Student, StudentView)
admin.site.register(Parent, ParentView)
admin.site.register(Statement, StatementView)
admin.site.register(Teacher, TeacherView)
admin.site.register(Year, YearView)
admin.site.register(Month, MonthView)
admin.site.register(Day, DayView)
admin.site.register(Offices, OfficesView)
admin.site.register(CallSchedule, CallScheduleView)
admin.site.register(Schedule, ScheduleView)
admin.site.register(Discipline, DisciplineView)
admin.site.register(TrainingClass, TrainingClassView)
admin.site.register(ListClasses, ListClassesView)
