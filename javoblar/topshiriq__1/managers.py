from django.contrib.auth.models import UserManager


class SoftDeleteManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)
