from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post


# Create your views here.
def posts_list(request):
    """
    블로그 글 전체 목록
    """
    # 전체목록
    # Post.objects.all()
    posts = Post.objects.order_by("-created_at")
    return render(request, "board/post_list.html", {"posts": posts})
