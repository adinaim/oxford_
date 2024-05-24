from rest_framework import serializers

from .models import (
    EngSchoolPage,
    EngSchoolImages,
    EngSchoolInfo,
    EngSchoolInfoImages,
)


class EngSchoolCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngSchoolPage
        fields = '__all__'

    engschool_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        engschool_carousel = validated_data.pop('engschool_image_carousel')
        engschool_page = EngSchoolPage.objects.create(**validated_data)
        images = []
        for image in engschool_carousel:
            images.append(EngSchoolImages(page=engschool_page, image=image))
        EngSchoolImages.objects.bulk_create(images)
        engschool_page.save()
        return engschool_page
    
    
class EngSchoolPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngSchoolPage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = EngSchoolImageSerializer(
            instance.engschool_page_images.all(), many=True
        ).data
        representation['engschool_info'] = EngSchoolInfoSerializer(
            instance.engschool_info.all(), many=True
        ).data
        return representation


class EngSchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngSchoolPage
        fields = '__all__'

    
class EngSchoolImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngSchoolImages
        fields = 'image',


class EngSchoolInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngSchoolInfo
        fields = '__all__'

    engschool_info_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        engschool_info_carousel = validated_data.pop('engschool_info_image_carousel')
        engschool_info = EngSchoolInfo.objects.create(**validated_data)
        images = []
        for image in engschool_info_carousel:
            images.append(EngSchoolInfoImages(info=engschool_info, image=image))
        EngSchoolInfoImages.objects.bulk_create(images)
        engschool_info.save()
        return engschool_info

    
class EngSchoolInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngSchoolInfo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = EngSchoolInfoImageSerializer(
            instance.engschool_info_images.all(), many=True
        ).data
        return representation


class EngSchoolInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngSchoolInfo
        fields = '__all__'

    
class EngSchoolInfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngSchoolInfoImages
        fields = 'image',