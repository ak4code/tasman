from rest_framework import viewsets
from .serializers import ProjectSerializer, BoardSerializer, CardSerializer
from .models import Project, Board, Card


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.prefetch_related('boards')
    serializer_class = ProjectSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
