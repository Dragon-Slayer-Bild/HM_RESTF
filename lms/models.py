from django.db import models


class Сourse(models.Model):

    name = models.CharField(
        max_length=255, verbose_name="Курс", help_text="Введите курс"
    )

    description = models.TextField(
        verbose_name="содержимое",
        help_text="содержимое урока",
        blank=True,
        null=True,
    )

    course_image = models.ImageField(
        upload_to="lms/curse_image",
        verbose_name="Изображение курса",
        blank=True,
        null=True,
        help_text="Загрузите изображение курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.name}"


class Lesson(models.Model):

    name = models.CharField(
        max_length=255, verbose_name="Урок", help_text="Введите урок"
    )

    description = models.TextField(
        verbose_name="содержимое",
        help_text="содержимое урока",
        blank=True,
        null=True,
    )

    lesson_image = models.ImageField(
        upload_to="lms/lessons_image",
        verbose_name="Изображение урока",
        blank=True,
        null=True,
        help_text="Загрузите изображение урока",
    )
    video_link = models.URLField(
        verbose_name="Ссылка ну урок",
        blank=True,
        null=True,
        help_text="Добавьте ссылку на урок",
    )
    course_id = models.ForeignKey(
        Сourse,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        related_name="course",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.name}"
