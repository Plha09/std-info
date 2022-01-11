from rest_framework import serializers
from std_info.models import Student


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ['id','Name','College','Email']