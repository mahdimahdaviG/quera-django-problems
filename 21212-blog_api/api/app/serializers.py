from .models import Post, Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Post
        fields = ["title", "body", "created", "owner"]


class PostDetailSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)
    comment_set = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comment_detail')

    class Meta:
        model = Post
        fields = ["title", "body", "created", "updated", "owner", "comment_set"]

class CommentSerializer(serializers.ModelSerializer):
    post = serializers.HyperlinkedRelatedField(read_only=True, view_name='post_detail')
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Comment
        fields = ["post", "owner", "body", "created", "updated"]