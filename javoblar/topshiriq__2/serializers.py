from rest_framework import serializers
from javoblar.topshiriq__2.models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = (
            'title',
            'content',
            'salary',
        )
