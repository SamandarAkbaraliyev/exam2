from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from javoblar.topshiriq__2.models import Vacancy
from javoblar.topshiriq__2.serializers import VacancySerializer
from javoblar.topshiriq__2.filters import VacancyFilter


class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [DjangoFilterBackend]

    filterset_class = VacancyFilter
