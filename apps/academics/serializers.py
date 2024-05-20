from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    AcademicsPage,
    AcademicsImages,
    AcademicsInfo,
    AcademicsInfoImages,
)


User = get_user_model()


class AcademicsCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = AcademicsPage
        fields = '__all__'

    academics_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        academics_carousel = validated_data.pop('academics_image_carousel')
        academics_page = AcademicsPage.objects.create(**validated_data)
        images = []
        for image in academics_carousel:
            images.append(AcademicsImages(page=academics_page, image=image))
        AcademicsImages.objects.bulk_create(images)
        academics_page.save()
        return academics_page

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs
    
    
class AcademicsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicsPage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = AcademicsImageSerializer(
            instance.academics_images.all(), many=True
        ).data
        representation['academics_info'] = AcademicsInfoSerializer(
            instance.academics_info.all(), many=True
        ).data
        return representation


class AcademicsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicsPage
        fields = '__all__'

    
class AcademicsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicsImages
        fields = 'image',


class AcademicsInfoCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = AcademicsInfo
        fields = '__all__'

    academics_info_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        academics_info_carousel = validated_data.pop('academics_info_image_carousel')
        academics_info = AcademicsInfo.objects.create(**validated_data)
        images = []
        for image in academics_info_carousel:
            images.append(AcademicsInfoImages(info=academics_info, image=image))
        AcademicsInfoImages.objects.bulk_create(images)
        academics_info.save()
        return academics_info

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs
    
    
class AcademicsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicsInfo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = AcademicsInfoImageSerializer(
            instance.academics_info_images.all(), many=True
        ).data
        return representation


class AcademicsInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicsInfo
        fields = '__all__'

    
class AcademicsInfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicsInfoImages
        fields = 'image',