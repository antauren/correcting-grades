import random

from datacenter.models import Mark, Schoolkid, Chastisement, Lesson, Commendation

COMENDATIONS = ['Молодец!',
                'Отлично!',
                'Хорошо!',
                'Гораздо лучше, чем я ожидал!',
                'Ты меня приятно удивил!',
                'Великолепно!',
                'Прекрасно!',
                'Ты меня очень обрадовал!',
                'Именно этого я давно ждал от тебя!',
                'Сказано здорово – просто и ясно!',
                'Ты, как всегда, точен!',
                'Очень хороший ответ!',
                'Талантливо!',
                'Ты сегодня прыгнул выше головы!',
                'Я поражен!',
                'Уже существенно лучше!',
                'Потрясающе!',
                'Замечательно!',
                'Прекрасное начало!',
                'Так держать!',
                'Ты на верном пути!',
                'Здорово!',
                'Это как раз то, что нужно!',
                'Я тобой горжусь!',
                'С каждым разом у тебя получается всё лучше!',
                'Мы с тобой не зря поработали!',
                'Я вижу, как ты стараешься!',
                'Ты растешь над собой!',
                'Ты многое сделал, я это вижу!',
                'Теперь у тебя точно все получится!']


def fix_marks(schoolkid_id, max_bad_points=3, good_points=5):
    bad_marks = Mark.objects.filter(schoolkid_id=schoolkid_id, points__lte=max_bad_points)

    for mark in bad_marks:
        mark.points = good_points
        mark.save()


def remove_chastisements(schoolkid_id):
    filtered_chastisements = Chastisement.objects.filter(schoolkid_id=schoolkid_id)
    filtered_chastisements.delete()


def create_commendation(schoolkid_id, subject_title):
    schoolkid = Schoolkid.objects.get(id=schoolkid_id)

    filtered_lessons = Lesson.objects.filter(
        subject__title__contains=subject_title,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
    )

    last_lesson = filtered_lessons.order_by('date').last()

    if last_lesson:
        text = random.choice(COMENDATIONS)

        Commendation.objects.create(text=text,
                                    created=last_lesson.date,
                                    schoolkid=schoolkid,
                                    subject=last_lesson.subject,
                                    teacher=last_lesson.teacher)


def print_schoolkids_ids(name):
    filtered_schoolkids = Schoolkid.objects.filter(full_name__contains=name)

    if filtered_schoolkids:

        for schoolkid in filtered_schoolkids:
            print(schoolkid.id, '\t', schoolkid)
    else:
        print('Учеников с таким именем нет в базе данных')
