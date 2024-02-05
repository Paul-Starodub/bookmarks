from typing import Optional

from django.contrib.auth.models import User
from django.http import HttpRequest

from account.models import Profile


def create_profile(
    backend: str, user: User, *args: tuple, **kwargs: dict
) -> None:
    Profile.objects.get_or_create(user=user)


class EmailAuthBackend:

    def authenticate(
        self,
        request: HttpRequest,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> Optional[User]:
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id: int) -> Optional[User]:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
