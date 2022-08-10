from django.views.generic import DetailView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ProjectSerializer, BoardSerializer, CardSerializer, ProjectBoardSerializer
from .models import Project, Board, Card


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.prefetch_related('boards', 'active_boards')
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['get'])
    def active_boards(self, request, pk=None):
        project = self.get_object()
        serializer = ProjectBoardSerializer(project.active_boards.all(), many=True)
        return Response(serializer.data)


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project-detail.html'
    pk_url_kwarg = 'project_id'
