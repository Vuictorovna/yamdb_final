import uuid

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from api_yamdb.settings import (ADMIN_EMAIL, CONFIRMATION_MESSAGE_TEMPLATE,
                                CONFIRMATION_MESSAGE_TOPIC)

from .serializers import AuthTokenSerializer, EmailSerializer


class AuthTokenView(TokenObtainPairView):
    serializer_class = AuthTokenSerializer


class EmailView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ["post"]

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        confirmation_code = uuid.uuid4()
        send_mail(
            CONFIRMATION_MESSAGE_TOPIC,
            CONFIRMATION_MESSAGE_TEMPLATE % confirmation_code,
            ADMIN_EMAIL,
            [email],
            fail_silently=False,
        )
        user = get_user_model().objects.create(username=email, email=email)
        user.set_password(confirmation_code)
        user.is_active = False
        user.save()

        return Response(serializer.validated_data)
