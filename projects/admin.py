from django.contrib import admin
from .models import Board,  Project, Card


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass
