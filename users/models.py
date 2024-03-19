from typing import Any

from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import CharField, DateTimeField
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from javoblar.topshiriq__1.managers import SoftDeleteManager


class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    deleted_at = DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = UserManager()

    def delete(self, using: Any = ..., keep_parents: bool = ...):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()

    def restore(self):
        self.deleted_at = None
        self.save()

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})
