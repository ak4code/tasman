from django.contrib import admin
from .models import Board, Project, ProjectBoard, Card


class ProjectBoardInlines(admin.StackedInline):
    model = ProjectBoard
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_absolute_url')
    filter_horizontal = ('boards',)
    inlines = (ProjectBoardInlines,)


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass
