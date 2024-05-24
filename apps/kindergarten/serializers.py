from rest_framework import serializers

from .models import (
    KindergartenPage,
    KindergartenImages,
    KindergartenInfo,
    KindergartenInfoImages,
)


class KindergartenCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindergartenPage
        fields = '__all__'

    kindergarten_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        kindergarten_carousel = validated_data.pop('kindergarten_image_carousel')
        kindergarten_page = KindergartenPage.objects.create(**validated_data)
        images = []
        for image in kindergarten_carousel:
            images.append(KindergartenImages(page=kindergarten_page, image=image))
        KindergartenImages.objects.bulk_create(images)
        kindergarten_page.save()
        return kindergarten_page
    
    
class KindergartenPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindergartenPage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = KindergartenImageSerializer(
            instance.kindergarten_page_images.all(), many=True
        ).data
        representation['kindergarten_info'] = KindergartenInfoSerializer(
            instance.kindergarten_info.all(), many=True
        ).data
        return representation


class KindergartenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindergartenPage
        fields = '__all__'

    
class KindergartenImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindergartenImages
        fields = 'image',


class KindergartenInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindergartenInfo
        fields = '__all__'

    kindergarten_info_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        kindergarten_info_carousel = validated_data.pop('kindergarten_info_image_carousel')
        kindergarten_info = KindergartenInfo.objects.create(**validated_data)
        images = []
        for image in kindergarten_info_carousel:
            images.append(KindergartenInfoImages(info=kindergarten_info, image=image))
        KindergartenImages.objects.bulk_create(images)
        kindergarten_info.save()
        return kindergarten_info

    
class KindergartenInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindergartenInfo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = KindergartenInfoImageSerializer(
            instance.kindergarten_info_images.all(), many=True
        ).data
        return representation


class KindergartenInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindergartenInfo
        fields = '__all__'

    
class KindergartenInfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindergartenInfoImages
        fields = 'image',