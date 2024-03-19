import django_filters
from javoblar.topshiriq__2.models import Vacancy


class VacancyFilter(django_filters.FilterSet):
    salary_from = django_filters.NumberFilter(field_name='salary', lookup_expr='gte')
    salary_to = django_filters.NumberFilter(field_name='salary', lookup_expr='lte')
    salary = django_filters.NumberFilter(field_name='salary', lookup_expr='exact')

    class Meta:
        model = Vacancy
        fields = (
            'salary_from',
            'salary_to',
            'salary',
        )
