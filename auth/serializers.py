from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AuthTokenSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().get_email_field_name()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].required = False

    def validate(self, attrs):
        attrs["password"] = self.context["request"].data.get(
            "confirmation_code"
        )
        return super().validate(attrs)


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
