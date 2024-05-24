from rest_framework import serializers

from .models import (
    RuSchoolPage,
    RuSchoolImages,
    RuSchoolInfo,
    RuSchoolInfoImages,
)


class RuSchoolCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuSchoolPage
        fields = '__all__'

    ruschool_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        ruschool_carousel = validated_data.pop('ruschool_image_carousel')
        ruschool_page = RuSchoolPage.objects.create(**validated_data)
        images = []
        for image in ruschool_carousel:
            images.append(RuSchoolImages(page=ruschool_page, image=image))
        RuSchoolImages.objects.bulk_create(images)
        ruschool_page.save()
        return ruschool_page
    
    
class RuSchoolPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuSchoolPage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = RuSchoolImageSerializer(
            instance.ruschool_page_images.all(), many=True
        ).data
        representation['ruschool_info'] = RuSchoolInfoSerializer(
            instance.ruschool_info.all(), many=True
        ).data
        return representation


class RuSchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuSchoolPage
        fields = '__all__'

    
class RuSchoolImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuSchoolImages
        fields = 'image',


class RuSchoolInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuSchoolInfo
        fields = '__all__'

    ruschool_info_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        ruschool_info_carousel = validated_data.pop('ruschool_info_image_carousel')
        ruschool_info = RuSchoolInfo.objects.create(**validated_data)
        images = []
        for image in ruschool_info_carousel:
            images.append(RuSchoolInfoImages(info=ruschool_info, image=image))
        RuSchoolInfoImages.objects.bulk_create(images)
        ruschool_info.save()
        return ruschool_info

    
class RuSchoolInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuSchoolInfo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = RuSchoolInfoImageSerializer(
            instance.ruschool_info_images.all(), many=True
        ).data
        return representation


class RuSchoolInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuSchoolInfo
        fields = '__all__'

    
class RuSchoolInfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuSchoolInfoImages
        fields = 'image',