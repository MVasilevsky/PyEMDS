from django.db import models

RANKS = (
    ('ml', 'Младший лейтенант'),
    ('le', 'Лейтенант'),
    ('sl', 'Старший лейтенант'),
    ('kp', 'Капитан'),
    ('mj', 'Майор'),
    ('pp', 'Подполковник'),
    ('pl', 'Полковник')
)


class Address(models.Model):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house = models.CharField(max_length=3)
    apartment = models.CharField(max_length=4, blank=True)


class Document(models.Model):
    DOCUMENT_TYPES = (
        ('statement', 'Заявление'),
        ('questionnaire', 'Анкета'),
        ('passport_copy', 'Ксерокопия паспорта'),
        ('registration_certificate_copy', 'Ксерокопия приписного свидетельства'),
        ('characteristic', 'Характеристика'),
        ('commission_direction', 'Направление на ВВК'),
        ('commission_certificate', 'Справка ВВК')
    )
    type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)


class DocumentInfo(models.Model):
    is_brought = models.BooleanField(default=False)
    commentary = models.CharField(max_length=500)


class Specialty(models.Model):
    title = models.CharField(max_length=100)


class Group(models.Model):
    title = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty)


class Questionnaire(models.Model):
    birth_place = models.CharField(max_length=50)
    # other fields here..


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)


class Student(Person):
    STUDENT_TYPES = (
        ('abiturient', 'Абитуриент'),
        ('junior', '1 этап обучения'),
        ('officer', '2 этап обучения'),
        ('reserve', 'Зачислен в запас'),
        ('failed', 'Отчислен'),
    )

    birth_date = models.DateField()
    group = models.ForeignKey(Group)
    questionnaire = models.OneToOneField(Questionnaire, primary_key=True)
    characteristic = models.CharField(max_length=10000)
    rank = models.CharField(max_length=20, choices=RANKS)
    type = models.CharField(max_length=10, choices=STUDENT_TYPES)


class StudentDocuments(models.Model):
    student = models.ForeignKey(Student)
    document = models.ForeignKey(Document)
    document_info = models.ForeignKey(DocumentInfo)


class Teacher(Person):
    rank = models.CharField(max_length=20, choices=RANKS)


