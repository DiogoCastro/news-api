from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for Article
    """

    time_since_publication = serializers.SerializerMethodField()

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    class Meta:
        model = Article
        fields = '__all__'

    def validate(self, data):
        """
        Check that description and title are different
        """
        title = data['title'].upper()
        desc = data['description'].upper()
        
        if title == desc:
            raise serializers.ValidationError('Title and Description must be different')
        return data

    def validate_title(self, value):
        """
        Check that the title have at least 30 chars
        """
        if len(value) < 30:
            raise serializers.ValidationError('The title has to be at least 30 chars long.')
        return value


class JournalistSerializer(serializers.ModelSerializer):
    """
    Serializer fot Journalist
    """

    articles = serializers.HyperlinkedRelatedField(many=True,
                                                   read_only=True,
                                                   view_name='article-detail')

    class Meta:
        model = Journalist
        fields = '__all__'