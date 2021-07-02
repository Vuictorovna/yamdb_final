from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, password=None, **kwargs):
        UserModel = get_user_model()  # noqa: N806

        try:
            if "email" in kwargs:
                user = UserModel.objects.get(email=kwargs["email"])
            else:
                user = UserModel.objects.get(username=kwargs["username"])

        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                user.is_active = True
                user.save()
                return user
        return None
