from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('__all__')
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id","Author_id", "text", "replies","parent_id"]
    def to_representation(self, instance):
        self.fields['replies'] = CommentSerializer(many=True, read_only=True)
        return super(CommentSerializer, self).to_representation(instance)
