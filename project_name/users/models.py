from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models

# Create your models here.


# BaseUserManager - User 생성 헬퍼 클래스
class CustomUserManager(BaseUserManager):
    # 회원정보 - 이메일, 닉네임, 비밀번호
    def _create_user(self, email, nickname, password, **extra_fields):
        if not email:
            raise ValueError("이메일 주소를 입력해주세요")
        if not nickname:
            raise ValueError("닉네임을 입력해주세요")
        user = self.model(email=self.normalize_email(email),
                          nickname=nickname,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, nickname, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, nickname, password, **extra_fields)

    def create_superuser(self, email, nickname, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("스태프 권한이 필요합니다")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser 권한이 필요합니다")
        return self._create_user(email, nickname, password, **extra_fields)

    # 실제 User 모델 -
    # AbstractUser(기본 필드와 권한 모두 가져옴) ,
    # AbstractBaseUser(password, last_login, is_active 필드만 존재 나머지 커스텀) 상속받아 생성
    # PermissionMixin


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="이메일 주소",
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(verbose_name="닉네임", max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_on = models.DateTimeField(verbose_name="생성 날짜", auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = "사용자 그룹"
        ordering = ["-created_on"]

    def __str__(self):
        return self.nickname
