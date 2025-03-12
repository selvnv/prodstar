### Задание

Давай создадим несложную, но вполне действенную вещь: базу данных сотрудников организации. У нас будут таблички “Сотрудники”, “Отделы” и “Филиалы”. Тебе предстоит создать таблицы в базе данных (через модели), прописать в них поля (Fields) правильных типов, определить и создать связи между этими таблицами (Foreign Key). Вот что конкретно потребуется хранить:

Для каждого Сотрудника нужны:

* Полное имя (обязательное поле)
* Должность (тоже обязательно)
* Номер телефона
* Дата рождения
* Email

Для каждого Отдела нужны (и обязательны):

* Название отдела (Например “Отдел маркетинга”, “Технический отдел”)
* Этаж, на котором расположен отдел (для простоты примем, что ни один отдел не может занимать более одного этажа)

Для каждого Филиала нужны:

* Адрес филиала (Например, “Москва, ул. 1905 года, д. 7, строение 1”)
* Короткое название (Например “На 1905 года”)

Сотрудник работает в каком-либо отделе. Отдел принадлежит какому-либо филиалу.

 
Давай сделаем, чтобы при удалении филиала все отделы, которые относились к этому филиалу оставались без указания на филиал. При удалении же отдела пусть все его сотрудники удаляются каскадно!

#### Что тебе нужно сделать

Для начала создай приложение

* Создай новый проект Django, добавь в него приложение “company”
* Придумай наиболее корректные названия полей, опиши модели Сотрудника, Отдела и Филиала в приложении “company”.
* Установи между моделями связи ForeignKey
* Сгенерируй миграции и примени их
* Заполни таблицы тестовыми данными: пусть будет минимум три филиала, в каждом от двух до пяти отделов, в каждом от одного до 30 сотрудников

Теперь напиши ряд запросов с помощью твоих моделей. Начнем с запросов, которые ты можешь выполнить по материалам урока:

* Получи количество сотрудников с должностью “Менеджер”
* Получи список сотрудников, работающих на четвертых этажах
* У тебя должно быть минимум три филиала. Узнай ID двух из них, и получи список всех сотрудников, работающих в этих двух филиалах, с помощью Q

Запросы, ради которых тебе придется погуглить:

* Получи список сотрудников, работающих в тех же двух филиалах из прошлого вопроса, только вместо Q используй лукап, проверяющий вхождение ID в список
* Получи список ФИО сотрудников, у которых не указан email
* Получи список сотрудников, чей год рождения 1990.

Для сдачи домашнего задания скопируй сюда описание моделей из файла company/models.py, а также пронумерованные запросы из секций выше. Если какие-то запросы написать не удалось, поставь прочерк под номером запроса.

Обрати внимание: не нужно писать циклы и принты, для проверки задания интересуют лишь сами запросы, которые вернут нужные Queryset.

### Выполнение

* Создание Django-проекта: `django-admin startproject orm .` 
* Создание сервиса: `py .\manage.py startapp company`
* Регистрация сервиса - `company` добавлен в `INSTALLED_APPS` (`settings.py`)
* Генерация данных - использован пакет `Faker` (добавлен в dev зависимости)
* Для просмотра базы данных использована программа `DB Browser for SQLite`

#### Запросы
Количество сотрудников-менеджеров
```python
In [37]: Employee.objects.filter(post__icontains='manager').count()
Out[37]: 14
```

Сотрудники, работающие на 4 этаже (отделы которых находятся на 4 этаже)
```python
Employee.objects.filter(department__floor=4).prefetch_related('department')
```

Т.к. нет ни одного такого сотрудника, дополнительно сделал запрос для сотрудников на 1 этаже. Список обширный, в блоке кода только часть вывода


```python
In [59]: employees = Employee.objects.filter(department__floor=1).prefetch_related('department')

In [60]: for e in employees:
    ...:     print(e.fullname, e.post)
    ...:
Benjamin Mason Financial planner
Lisa Compton Nurse, children's
Carmen Curry Intelligence analyst
Jose Quinn Therapist, art
Eileen Alexander Network engineer
Jeremy Henry Armed forces operational officer
John Decker Physiotherapist
Paul Cabrera Programmer, multimedia
Dawn Lara DVM Research scientist (physical sciences)
Dana Howe Jewellery designer
...
```
Для просмотра запросов и очистки очереди выполненных запросов импортировал `connection.queries` и `reset_queries()` из `django.db`

Объект `Q` импортируется при помощи `from django.db.models import Q`

Список сотрудников из филиалов 1 и 2 при помощи `Q`
```python
BranchOffice.objects.filter(Q(pk=1) | Q(pk=2)).prefetch_related('departments', 'departments__employees').values_list('departments__employees__fullname', flat=True)
```
```python
In [76]: employees_dep_1_or_2 = BranchOffice.objects.filter(Q(pk=1) | Q(pk=2)).prefetch_related('departments', 'departments__employees').values_list('departments__employees__fullname', flat=True)

In [77]: for e in employees_dep_1_or_2:
    ...:     print(e)
    ...:
Benjamin Mason
Lisa Compton
Carmen Curry
Jose Quinn
Eileen Alexander
Jeremy Henry
John Decker
Paul Cabrera
Dawn Lara DVM
Dana Howe
Susan Donovan
Autumn Lee
...
```
Количество сотрудников в этих филиалах:
```python
In [79]: print(BranchOffice.objects.filter(Q(pk=1) | Q(pk=2)).prefetch_related('departments', 'departments__employees').values_list('departments__employees__fullname', flat=True).count())
151
```
Количество сотрудников в филиалах 1, 2 с использованием `__in`:
```python
 BranchOffice.objects.filter(pk__in=[1, 2]).prefetch_related('departments', 'departments__employees').values_list('departments__employees__fullname', flat=True)
```

Сотрудники, у которых `email is NULL`
```python
# Предварительно проставил NULL в поле email у нескольких сотрудников
In [86]: Employee.objects.filter(pk__in=[1, 50, 100, 200]).update(
    ...:     email=None
    ...: )
Out[86]: 4

# Запрос с проверкой на NULL
In [89]: employees = Employee.objects.filter(email=None).values('fullname', 'email', 'post')

In [90]: for e in employees:
    ...:     print(e)
    ...:
{'fullname': 'Aaron Bennett', 'email': None, 'post': 'Engineer, water'}
{'fullname': 'Charles Gonzalez', 'email': None, 'post': 'Forensic psychologist'}
{'fullname': 'Hannah Richards', 'email': None, 'post': 'Chief Marketing Officer'}
{'fullname': 'Laura Nelson', 'email': None, 'post': 'Geologist, wellsite'}
```

Сотрудники с годом рождения 1990
```python
In [102]: employees = Employee.objects.filter(birth_date__year=1990).values('fullname', 'birth_date')

In [103]: for e in employees:
     ...:     print(e)
     ...:
{'fullname': 'Regina Anderson', 'birth_date': datetime.date(1990, 2, 22)}
```