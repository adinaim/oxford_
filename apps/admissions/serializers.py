from rest_framework import serializers

from .models import (
    AdmissionsPage,
    AdmissionsImages,
    AdmissionsInfo,
    AdmissionsInfoImages,
)


class AdmissionsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsPage
        fields = '__all__'

    admissions_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        admissions_carousel = validated_data.pop('admissions_image_carousel')
        admissions_page = AdmissionsPage.objects.create(**validated_data)
        images = []
        for image in admissions_carousel:
            images.append(AdmissionsImages(page=admissions_page, image=image))
        AdmissionsImages.objects.bulk_create(images)
        admissions_page.save()
        return admissions_page
    
    
class AdmissionsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsPage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = AdmissionsImageSerializer(
            instance.admissions_images.all(), many=True
        ).data
        representation['admissions_info'] = AdmissionsInfoSerializer(
            instance.admissions_info.all(), many=True
        ).data
        return representation


class AdmissionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsPage
        fields = '__all__'

    
class AdmissionsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsImages
        fields = 'image',


class AdmissionsInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsInfo
        fields = '__all__'

    admissions_info_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        admissions_info_carousel = validated_data.pop('admissions_info_image_carousel')
        admissions_info = AdmissionsInfo.objects.create(**validated_data)
        images = []
        for image in admissions_info_carousel:
            images.append(AdmissionsInfoImages(info=admissions_info, image=image))
        AdmissionsInfoImages.objects.bulk_create(images)
        admissions_info.save()
        return admissions_info
    
    
class AdmissionsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsInfo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = AdmissionsInfoImageSerializer(
            instance.admissions_info_images.all(), many=True
        ).data
        return representation


class AdmissionsInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsInfo
        fields = '__all__'

    
class AdmissionsInfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionsInfoImages
        fields = 'image',