<<<<<<< HEAD
from typing import Any

from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import CharField, DateTimeField
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from javoblar.topshiriq__1.managers import SoftDeleteManager


class User(AbstractUser):
=======
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
>>>>>>> 4ae7687d27840c5702f8c4672c9a57d2eafc5777
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

<<<<<<< HEAD
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
=======
    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
>>>>>>> 4ae7687d27840c5702f8c4672c9a57d2eafc5777
        return reverse("users:detail", kwargs={"username": self.username})
