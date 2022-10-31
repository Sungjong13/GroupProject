from django.db import models
from users.models import User

from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):
    # 게시글 모델 - 카테고리, 제목, 내용, 태그, 첨부파일, 작성날짜, 수정날짜
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField()
    tags = TaggableManager(blank=True)
    file = models.FileField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 작성날짜
    modified_at = models.DateTimeField(auto_now=True)  # 수정날짜

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    pass
