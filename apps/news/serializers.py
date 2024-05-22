from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import (
    News, 
    NewsImage,
    Event,
    EventImage
)


User = get_user_model()


class NewsCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = News
        fields = '__all__'

    news_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        news_carousel = validated_data.pop('news_image_carousel')
        news = News.objects.create(**validated_data)
        images = []
        for image in news_carousel:
            images.append(NewsImage(news=news, image=image))
        NewsImage.objects.bulk_create(images)
        news.save()
        return news

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs
    
    
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = NewsImageSerializer(
            instance.news_images.all(), many=True
        ).data
        return representation


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    
class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = 'image',


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    event_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        event_carousel = validated_data.pop('event_image_carousel')
        event = Event.objects.create(**validated_data)
        images = []
        for image in event_carousel:
            images.append(EventImage(event=event, image=image))
        EventImage.objects.bulk_create(images)
        event.save()
        return event

    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = NewsImageSerializer(
            instance.events_images.all(), many=True
        ).data
        return representation
    

# class EventImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EventImage
#         fields = 'image',