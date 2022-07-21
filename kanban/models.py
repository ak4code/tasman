from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    boards = models.ManyToManyField('Board', verbose_name='Доски')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Board(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'


class Card(models.Model):
    project = models.ForeignKey('Project', blank=True, null=True, related_name='cards', on_delete=models.CASCADE, verbose_name='Проект')
    board = models.ForeignKey('Board', blank=True, null=True, related_name='cards', on_delete=models.CASCADE, verbose_name='Доска')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
