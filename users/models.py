from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email), username=username, **kwargs
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password=None, **kwargs):
        return self.create_user(
            email,
            username=username,
            password=password,
            is_superuser=True,
            is_staff=True,
            role=User.ADMIN,
            **kwargs
        )


class User(AbstractBaseUser, PermissionsMixin):
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"

    ROLES_CHOICES = [
        (USER, "user"),
        (MODERATOR, "moderator"),
        (ADMIN, "admin"),
    ]

    first_name = models.CharField("first name", max_length=30, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    username = models.CharField("username", max_length=30, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True
    )
    role = models.CharField(
        max_length=20,
        choices=ROLES_CHOICES,
        default=USER,
    )
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )

    objects = UserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        ordering = ["-id"]

    @property
    def is_user_admin(self):
        return self.role == User.ADMIN

    @property
    def is_user_moderator(self):
        return self.role == User.MODERATOR
