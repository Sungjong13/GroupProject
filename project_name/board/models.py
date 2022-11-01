from django.db import models
from users.models import User

from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):
    # 게시글 모델 - 카테고리, 제목, 내용, 태그, 첨부파일, 작성날짜, 수정날짜, 조회수
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="작성자")
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=30, blank=False, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    tags = TaggableManager(blank=True)
    image = models.ImageField(null=True,
                              blank=True,
                              upload_to="users_upload/%Y/%m/%d")
    created_at = models.DateTimeField(auto_now_add=True)  # 작성날짜
    modified_at = models.DateTimeField(auto_now=True)  # 수정날짜

    def __str__(self) -> str:
        return self.title


class Answer(models.Model):
    # 답변 모델 - 작성자, 질문,
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="작성자")
    question = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="답변 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성 날짜")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="수정 날짜")


class Comment(models.Model):
    # 댓글 모델 - 작성자, 내용, 작성날짜, 수정날짜, 답변내용
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="작성자")
    content = models.TextField(verbose_name="댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성 날짜")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="수정 날짜")
    answer = models.ForeignKey(Answer,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               verbose_name="답변")
