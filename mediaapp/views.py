from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article,Comment

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comment.objects.filter(parent=None)
    serializer_class = CommentSerializer