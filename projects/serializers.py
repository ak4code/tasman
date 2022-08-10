from rest_framework import serializers

from .models import Project, ProjectBoard, Board, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class ProjectBoardSerializer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True, many=True)

    class Meta:
        model = ProjectBoard
        fields = ['id', 'board', 'cards', 'name']


class ProjectSerializer(serializers.ModelSerializer):
    active_boards = ProjectBoardSerializer(read_only=True, many=True)
    link = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
