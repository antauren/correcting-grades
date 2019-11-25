# Скрипт для взлома электронного дневника школы

С помощью данного скрипта можно улучшить оценки, удалить замечания учителя и даже получить от него хвалебный отзыв

## Описание скрипта

Скрипт содержит четыре функции: 
- `fix_marks` — исправит оценки ученика (двойки и тройки превратятся в пятерки)
- `create_commendation` — добавит похвалу от учителя, за особые достижения на последнем уроке
- `remove_chastisements` — удялит замечания от учителя, за особые проступки
- `print_schoolkids_ids` — поможет найти `id` ученика по имени 
(необходимо для работы вышеперечисленных функций)


## Запуск
- зайдите в корневой каталог электронного дневника
- положите файл `scripts.py` в корневой каталог (рядом с `manage.py`)
- Зайдите в Shell в консоли командой `python manage.py shell`
- Импортируйте все функции скрипта одной командой: `from scripts import *`
- Введите команду (см. примеры ниже)

## Примеры
Допустим нужно исправить информацию про Анатолия Голубева  
Необходимо точно знать его `id`, которые нужно указать при запуске других функций

### Поиск `id` ученика
```
>>> print_schoolkids_ids('Голубев Ан')
6251     Голубев Анатолий Тимурович 2В
6410     Голубев Андроник Анисимович 4Б
```

### Исправление оценок ученика
```
>>> fix_marks(6251)
```

### Удаление замечаний
```
>>> remove_chastisements(6251)
```

### Добавить хвалебный отзыв учителя по нужному предмету
```
>>> create_commendation(6251, 'Музыка')
```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
