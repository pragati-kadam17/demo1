from rest_framework import fields,serializers
from .models import Patient, Test, LabTest

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'gender', 'address']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'name', 'price']

class LabTestSerializer(serializers.ModelSerializer):
    test = serializers.PrimaryKeyRelatedField(queryset=Test.objects.all())
    #test = TestSerializer(many=True)
    #patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = LabTest
        fields = ['patient', 'test', 'date','price'
        ]


class LabHeadSignUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_lab_head=True
        )
        return user

class PatientSignUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_patient=True
        )
        return user



