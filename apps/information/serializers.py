from rest_framework import serializers

from .models import (
    AboutUsPage,
    AboutUsPageImage,
    AboutUsInfo,
    AboutUsInfoImage,
    Information
)


class AboutUsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsPage
        fields = '__all__'

    about_us_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        about_us_carousel = validated_data.pop('about_us_image_carousel')
        about_us_page = AboutUsPage.objects.create(**validated_data)
        images = []
        for image in about_us_carousel:
            images.append(AboutUsPageImage(page=about_us_page, image=image))
        AboutUsPageImage.objects.bulk_create(images)
        about_us_page.save()
        return about_us_page
    
    
class AboutUsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsPage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = AboutUsImageSerializer(
            instance.about_us_images.all(), many=True
        ).data
        representation['about_us_info'] = AboutUsInfoSerializer(
            instance.about_us_info.all(), many=True
        ).data
        return representation


class AboutUsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsPage
        fields = '__all__'

    
class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsPageImage
        fields = 'image',


class AboutUsInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsInfo
        fields = '__all__'

    about_us_info_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        about_us_info_carousel = validated_data.pop('about_us_info_image_carousel')
        about_us_info = AboutUsInfo.objects.create(**validated_data)
        images = []
        for image in about_us_info_carousel:
            images.append(AboutUsInfoImage(info=about_us_info, image=image))
        AboutUsInfoImage.objects.bulk_create(images)
        about_us_info.save()
        return about_us_info
    
    
class AboutUsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsInfo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = AboutUsInfoImageSerializer(
            instance.about_us_info_images.all(), many=True
        ).data
        return representation


class AboutUsInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsInfo
        fields = '__all__'

    
class AboutUsInfoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsInfoImage
        fields = 'image',


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'