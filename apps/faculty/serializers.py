from rest_framework import serializers

from .models import (
    Department,
    DepartmentImage,
    Faculty
)


class DepartmentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'

    department_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )

    def create(self, validated_data):
        department_carousel = validated_data.pop('department_image_carousel')
        department = Department.objects.create(**validated_data)
        images = []
        for image in department_carousel:
            images.append(DepartmentImage(page=department, image=image))
        DepartmentImage.objects.bulk_create(images)
        department.save()
        return department
    
    
class DepartmentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = DepartmentImageSerializer(
            instance.department_images.all(), many=True
        ).data
        representation['department_faculty'] = FacultySerializer(
            instance.department_faculty.all(), many=True
        ).data
        return representation


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    
class DepartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentImage
        fields = 'image',


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('first_name', 'last_name', 'image', 'department', 'position')