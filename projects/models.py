from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    boards = models.ManyToManyField('Board', through='ProjectBoard', verbose_name='Доски')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        :return: '/projects/{id}/'
        """
        return reverse('projects:project-detail', kwargs={'project_id': self.pk})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectBoard(models.Model):
    project = models.ForeignKey('Project', related_name='active_boards', on_delete=models.CASCADE,
                                verbose_name='Проект')
    board = models.ForeignKey('Board', on_delete=models.CASCADE, verbose_name='Доска')
    active = models.BooleanField(default=True, verbose_name='Активная доска')

    @property
    def name(self):
        return self.board.name

    def __str__(self):
        return self.board.name

    class Meta:
        verbose_name = 'Доска проекта'
        verbose_name_plural = 'Доски проекта'


class Board(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'


class Card(models.Model):
    board = models.ForeignKey('ProjectBoard', related_name='cards', on_delete=models.CASCADE, verbose_name='Доска')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
